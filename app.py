# app.py - 应用主程序
import sys
import os

# 将本地lib目录添加到Python模块搜索路径
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib"))

import json
import logging
import random
import traceback
import time
from functools import partial
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QApplication
import re

from LoginUi import Ui_LoginWindow
from InterfaceUi import Ui_MainWindow
import db, utils

# 确保数据库存在并可选导入示例数据
db.ensure_tables()
if os.path.exists("sample_questions.json"):
    try:
        qs = db.load_questions(limit=1)
        if len(qs) == 0:
            n = db.import_questions_from_json_file("sample_questions.json")
            print(f"Imported {n} sample questions.")
    except Exception as e:
        print("No sample import:", e)

# 日志配置
logging.basicConfig(filename="app_error.log", level=logging.DEBUG,
                    format="%(asctime)s %(levelname)s %(message)s")


def _excepthook(type_, value, tb):
    logging.error("未捕获的异常", exc_info=(type_, value, tb))
    print("未捕获的异常（详见app_error.log）:", value)


sys.excepthook = _excepthook


def parse_txt_questions(path: str):
    """
    从简单的 TXT 格式解析题目，返回 list[dict]
    每题之间用空行分隔。解析尽量容错。
    输出题目格式：
    { "subject": None|"科目名称", "unit": None|int, "stem": "...", "type": "single|multi|text",
      "options": [...], "answer": [...], "analysis": "..." }
    """
    questions = []
    try:
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
    except Exception as e:
        print("parse_txt_questions: 打开文件失败", e)
        return []

    blocks = re.split(r'\n\s*\n', text.strip(), flags=re.MULTILINE)
    for block in blocks:
        lines = [ln.rstrip() for ln in block.splitlines() if ln.strip() != ""]
        if not lines:
            continue
        q = {"subject": None, "unit": None, "stem": "", "type": "single", "options": [], "answer": [], "analysis": ""}

        i = 0
        while i < len(lines):
            line = lines[i].strip()
            # 通过"Q:"或"1. "格式检测题目题干
            m = re.match(r'^(?:Q|Question)\s*[:\.]\s*(.+)', line, re.I)
            if m:
                q["stem"] = m.group(1).strip()
                i += 1
                continue
            m = re.match(r'^\d+\.\s*(.+)', line)
            if m and q["stem"] == "":
                q["stem"] = m.group(1).strip()
                i += 1
                continue
            # 题目类型
            m = re.match(r'^(?:Type|类型)\s*[:：]\s*(.+)', line, re.I)
            if m:
                q["type"] = m.group(1).strip().lower()
                i += 1
                continue
            # 科目
            m = re.match(r'^(?:Subject|科目)\s*[:：]\s*(.+)', line, re.I)
            if m:
                q["subject"] = m.group(1).strip()
                i += 1
                continue
            # 单元
            m = re.match(r'^(?:Unit|单元)\s*[:：]\s*(\d+)', line, re.I)
            if m:
                try:
                    q["unit"] = int(m.group(1))
                except Exception:
                    q["unit"] = m.group(1).strip()
                i += 1
                continue
            # 选项块
            if re.match(r'^(?:Options|选项)\s*[:：]?', line, re.I):
                i += 1
                while i < len(lines):
                    l2 = lines[i].strip()
                    if re.match(r'^(?:Answer|答案|Analysis|解析|Type|类型|Subject|科目|Unit|单元)\s*[:：]', l2, re.I):
                        break
                    mopt = re.match(r'^[A-Za-z]\s*[\.\、\)]\s*(.+)', l2)
                    if mopt:
                        q["options"].append(mopt.group(1).strip())
                    else:
                        parts = re.split(r'[；;]\s*', l2)
                        if len(parts) > 1:
                            for p in parts:
                                p = re.sub(r'^[A-Za-z]\s*[\.\、\)]\s*', '', p).strip()
                                if p:
                                    q["options"].append(p)
                        else:
                            q["options"].append(l2)
                    i += 1
                continue
            # 单行选项格式 A. ...
            mopt = re.match(r'^[A-Za-z]\s*[\.\、\)]\s*(.+)', line)
            if mopt:
                q["options"].append(mopt.group(1).strip())
                i += 1
                continue
            # Answer
            m = re.match(r'^(?:Answer|答案)\s*[:：]\s*(.+)', line, re.I)
            if m:
                ans_raw = m.group(1).strip()
                parts = re.split(r'[,;；\s]+', ans_raw)
                parts = [p.strip().upper() for p in parts if p.strip() != ""]
                q["answer"] = parts
                i += 1
                continue
            # Analysis
            m = re.match(r'^(?:Analysis|解析)\s*[:：]\s*(.*)', line, re.I)
            if m:
                buf = [m.group(1).strip()]
                i += 1
                while i < len(lines):
                    nxt = lines[i].strip()
                    if re.match(r'^(?:Answer|答案|Options|选项|Type|类型|Subject|科目|Unit|单元)\s*[:：]', nxt, re.I):
                        break
                    buf.append(nxt)
                    i += 1
                q["analysis"] = "\n".join([b for b in buf if b])
                continue
            # fallback: part of stem
            if q["stem"] == "":
                q["stem"] = line
            else:
                q["stem"] = q["stem"] + "\n" + line
            i += 1

        # infer type if unclear
        if q["type"] not in ("single", "multi", "text"):
            if isinstance(q["answer"], list) and len(q["answer"]) > 1:
                q["type"] = "multi"
            else:
                q["type"] = "single"

        questions.append(q)

    return questions


class LogWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)

        # show/hide password button
        self.show_pwd_btn = QtWidgets.QPushButton("👁", self.ui.Login)
        self.show_pwd_btn.setFixedSize(28, 24)
        try:
            self.show_pwd_btn.setGeometry(220, 40, 28, 24)
        except Exception:
            pass
        self.show_pwd_btn.clicked.connect(self.toggle_pwd_visibility)

        # registration password fields hide
        try:
            self.ui.lineEdit_R_password1.setEchoMode(QtWidgets.QLineEdit.Password)
            self.ui.lineEdit_R_password2.setEchoMode(QtWidgets.QLineEdit.Password)
        except Exception:
            pass

        # connect login / register
        self.ui.button_L_sure.clicked.connect(self.login_in)
        self.ui.pushButton_R_sure.clicked.connect(self.register_user)

        # switch stacked login/register pages
        try:
            self.ui.pushButton_Login.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentIndex(0))
            self.ui.pushButton_Register.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentIndex(1))
        except Exception:
            pass

        self.user_id = None

    def toggle_pwd_visibility(self):
        try:
            if self.ui.line_L_password.echoMode() == QtWidgets.QLineEdit.Password:
                self.ui.line_L_password.setEchoMode(QtWidgets.QLineEdit.Normal)
                self.show_pwd_btn.setText("🙈")
            else:
                self.ui.line_L_password.setEchoMode(QtWidgets.QLineEdit.Password)
                self.show_pwd_btn.setText("👁")
        except Exception:
            pass

    def register_user(self):
        username = self.ui.lineEdit_R_account.text().strip()
        p1 = self.ui.lineEdit_R_password1.text()
        p2 = self.ui.lineEdit_R_password2.text()
        if not username or not p1 or not p2:
            QMessageBox.warning(self, "注册失败", "账号或密码不能为空")
            return
        if p1 != p2:
            QMessageBox.warning(self, "注册失败", "两次密码不一致")
            return
        salt, h = utils.hash_password(p1)
        ok = db.add_user(username, salt, h)
        if ok:
            QMessageBox.information(self, "注册成功", "注册成功，请登录")
            try:
                self.ui.stackedWidget_2.setCurrentIndex(0)
            except Exception:
                pass
        else:
            QMessageBox.warning(self, "注册失败", "账号已存在或注册失败")

    def login_in(self):
        account = self.ui.line_L_account.text().strip()
        password = self.ui.line_L_password.text()
        if not account or not password:
            QMessageBox.warning(self, "登录失败", "账号或密码不能为空")
            return
        row = db.get_user(account)
        if not row:
            QMessageBox.warning(self, "登录失败", "账号或密码错误")
            return
        user_id, username, salt_hex, hash_hex = row
        if utils.verify_password(salt_hex, hash_hex, password):
            self.main = MainWindow(user_id, username)
            self.main.show()
            self.close()
        else:
            QMessageBox.warning(self, "登录失败", "账号或密码错误")


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, user_id: int, username: str):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # --- debug & ensure import button binding (粘在 setupUi(self) 之后) ---
        try:
            # 列出 ui 中所有包含 pushButton 的属性，帮助定位实际名字
            pushbtn_attrs = [a for a in dir(self.ui) if "pushbutton" in a.lower()]
            print("DEBUG: ui pushButton attributes found:", pushbtn_attrs)

            # 如果确实存在 pushButton_import，就绑定；否则尝试绑定到 confirm_import 作为后备
            if hasattr(self.ui, "pushButton_import"):
                btn = getattr(self.ui, "pushButton_import")
                try:
                    btn.clicked.disconnect()
                except Exception:
                    pass
                # 优先连接到 _on_import_button（我们在类里实现），否则连接 confirm_import
                handler = getattr(self, "_on_import_button", None) or getattr(self, "confirm_import", None)
                if handler is not None:
                    btn.clicked.connect(handler)
                    print("DEBUG: Bound import button: pushButton_import ->", handler.__name__)
                else:
                    print("DEBUG: Found pushButton_import but no handler _on_import_button / confirm_import present")
            else:
                print("DEBUG: pushButton_import not found on self.ui (check InterfaceUi.py)")
        except Exception as e:
            print("DEBUG: exception during import-button bind:", e)

        self.user_id = user_id
        self.username = username
        self.setWindowTitle(f"HopeBox - {self.username}")

        # state
        self.questions = db.load_questions() or []
        self.max_questions = 10
        self.cur_index = 0
        self.selected_subject = None
        self.finished = False
        self.in_wrong_mode = False

        # 每页动态容器用于选项组件
        self.options_containers = {}
        self.current_option_widgets = []
        self.current_options_page = None
        self.option_button_group = None

        # 错题缓存（字典列表）
        self._cached_wrongs = None

        # 小型占位符以保持UI布局稳定（不直接使用）
        try:
            self.options_widget = QtWidgets.QWidget(self.ui.frame_12)
            self.options_layout = QtWidgets.QVBoxLayout(self.options_widget)
            self.options_layout.setContentsMargins(0, 0, 0, 0)
            if hasattr(self.ui, "verticalLayout_7"):
                try:
                    if self.ui.verticalLayout_7.indexOf(self.options_widget) == -1:
                        self.ui.verticalLayout_7.insertWidget(1, self.options_widget)
                except Exception:
                    pass
        except Exception:
            pass

        # 导航和控制绑定（防御性）
        try:
            self.ui.pushButton_home.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
            self.ui.pushButton_my.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
            self.ui.pushButton_module.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(3))
        except Exception:
            pass

        # 科目按钮（安全模式）
        try:
            self.ui.pushButton_MAX.clicked.connect(lambda: self.on_subject_clicked("马克思主义原理"))
            self.ui.pushButton_Moral.clicked.connect(lambda: self.on_subject_clicked("思想道德与法治"))
            self.ui.pushButton_Outline.clicked.connect(lambda: self.on_subject_clicked("中国近代史纲要"))
            self.ui.pushButton_Mao.clicked.connect(lambda: self.on_subject_clicked("毛泽东思想和中国特色社会主义理论体系概论"))
            self.ui.pushButton_Xi.clicked.connect(lambda: self.on_subject_clicked("习近平新时代中国特色社会主义思想"))
        except Exception:
            pass

        # 单元按钮 -> 开始练习
        try:
            self.ui.pushButton_fir.clicked.connect(lambda: self.start_practice(unit=1))
            self.ui.pushButton_sec.clicked.connect(lambda: self.start_practice(unit=2))
            self.ui.pushButton_thi.clicked.connect(lambda: self.start_practice(unit=3))
            self.ui.pushButton_fou.clicked.connect(lambda: self.start_practice(unit=4))
            self.ui.pushButton_fif.clicked.connect(lambda: self.start_practice(unit=5))
            self.ui.pushButton_six.clicked.connect(lambda: self.start_practice(unit=6))
            self.ui.pushButton_sev.clicked.connect(lambda: self.start_practice(unit=7))
            self.ui.pushButton_eig.clicked.connect(lambda: self.start_practice(unit=8))
            self.ui.pushButton_nin.clicked.connect(lambda: self.start_practice(unit=9))
            self.ui.pushButton_ten.clicked.connect(lambda: self.start_practice(unit=10))
        except Exception:
            pass

        # 导入功能（连接选择/确认按钮，如果存在的话）
        try:
            if hasattr(self.ui, "pushButton_5"):
                self.ui.pushButton_5.clicked.connect(self.choose_file)
            if hasattr(self.ui, "pushButton_9"):
                self.ui.pushButton_9.clicked.connect(self.confirm_import)
            # 注意：pushButton_import 之前已通过检测绑定处理
        except Exception:
            pass

        # 其他控制按钮
        try:
            self.ui.pushButton_wrong_return.clicked.connect(lambda: self.ui.stackedWidget_3.setCurrentIndex(0))
            self.ui.pushButton_logout.clicked.connect(self.logout)
            self.ui.pushButton_finish_return.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
            self.ui.pushButton_statistics_return.clicked.connect(lambda: self.ui.stackedWidget_3.setCurrentIndex(0))
        except Exception:
            pass

        # 刷新错题列表并绑定变更处理器（避免重复连接）
        try:
            self.refresh_wrong_list(limit=self.max_questions)
            try:
                self.ui.listWidget_wrong.currentRowChanged.disconnect(self.on_wrong_item_changed)
            except Exception:
                pass
            self.ui.listWidget_wrong.currentRowChanged.connect(self.on_wrong_item_changed)
        except Exception:
            pass

        # 练习导航/提交按钮绑定
        try:
            # 仍然绑定，但确保start_practice/start_wrong_practice也调用_bind_practice_nav_buttons
            self.ui.pushButton_next1.clicked.connect(lambda: self.next_question(1))
            self.ui.pushButton_next2.clicked.connect(lambda: self.next_question(1))
            self.ui.pushButton_next3.clicked.connect(lambda: self.next_question(1))
            self.ui.pushButton_18.clicked.connect(lambda: self.next_question(-1))
            self.ui.pushButton_last2.clicked.connect(lambda: self.next_question(-1))
            self.ui.pushButton_last3.clicked.connect(lambda: self.next_question(-1))

            self.ui.pushButton_show_answer1.clicked.connect(self.submit_current_answer)
            self.ui.pushButton_show_answer2.clicked.connect(self.submit_current_answer)
            self.ui.pushButton_show_answer3.clicked.connect(self.submit_current_answer)
        except Exception:
            pass

        # bind wrong-book buttons (try a couple of possible names)
        for btn_name in ("pushButton_wrong", "pushButton_wrong_book", "pushButton_open_wrong"):
            if hasattr(self.ui, btn_name):
                try:
                    getattr(self.ui, btn_name).clicked.connect(lambda _, s=self: s.start_wrong_practice(limit=self.max_questions, shuffle=False))
                except Exception:
                    pass

        # if list double-click should start wrong practice
        try:
            if hasattr(self.ui, "listWidget_wrong"):
                self.ui.listWidget_wrong.itemDoubleClicked.connect(lambda item, s=self: s.start_wrong_practice(limit=self.max_questions, shuffle=False))
        except Exception:
            pass

        # done init
        self.debug_print_stacked_pages()
        self.update_statistics_display()

    # convenience import-button handler used by debug binder
    def _on_import_button(self):
        """Open file dialog, set lineEdit and immediately call confirm_import()."""
        try:
            path, _ = QFileDialog.getOpenFileName(self, "选择题库文件", "", "JSON 文件 (*.json);;文本文件 (*.txt)")
            if path:
                try:
                    if hasattr(self.ui, "lineEdit"):
                        self.ui.lineEdit.setText(path)
                except Exception:
                    pass
                # call confirm_import to perform parsing/import
                try:
                    self.confirm_import()
                except Exception as e:
                    QMessageBox.critical(self, "导入失败", f"导入时发生错误：{e}")
        except Exception as e:
            print("_on_import_button error:", e)

    # ---------- navigation binding helpers ----------
    def _bind_practice_nav_buttons(self, practice_page_index: int):
        next_btn_names = ("pushButton_next1", "pushButton_next2", "pushButton_next3")
        prev_btn_names = ("pushButton_18", "pushButton_last2", "pushButton_last3")

        for name in next_btn_names:
            if hasattr(self.ui, name):
                try:
                    btn = getattr(self.ui, name)
                    try:
                        btn.clicked.disconnect()
                    except Exception:
                        pass
                    btn.clicked.connect(partial(self.next_question, 1))
                    btn.setEnabled(True)
                except Exception:
                    pass

        for name in prev_btn_names:
            if hasattr(self.ui, name):
                try:
                    btn = getattr(self.ui, name)
                    try:
                        btn.clicked.disconnect()
                    except Exception:
                        pass
                    btn.clicked.connect(partial(self.next_question, -1))
                    btn.setEnabled(True)
                except Exception:
                    pass

    def _update_nav_buttons_state(self):
        """修改点：允许在最后一题 (cur_index == total-1) 时仍启用 '下一题'，点击后会直接到完成页。"""
        total = len(self.questions) if hasattr(self, "questions") else 0
        prev_enabled = (self.cur_index > 0 and total > 0)
        next_enabled = (self.cur_index < total and total > 0)

        prev_btn_names = ("pushButton_18", "pushButton_last2", "pushButton_last3")
        next_btn_names = ("pushButton_next1", "pushButton_next2", "pushButton_next3")

        for name in prev_btn_names:
            if hasattr(self.ui, name):
                try:
                    getattr(self.ui, name).setEnabled(prev_enabled)
                except Exception:
                    pass
        for name in next_btn_names:
            if hasattr(self.ui, name):
                try:
                    getattr(self.ui, name).setEnabled(next_enabled)
                except Exception:
                    pass

        try:
            if hasattr(self.ui, "label_question_index"):
                total_text = total if total > 0 else 0
                getattr(self.ui, "label_question_index").setText(f"{self.cur_index + 1}/{total_text}")
        except Exception:
            pass

    # ---------- subject / debug ----------
    def on_subject_clicked(self, subject_name: str):
        try:
            self.selected_subject = subject_name
            target_index = 2
            try:
                sw = getattr(self.ui, "stackedWidget", None)
                if sw is not None:
                    for i in range(sw.count()):
                        w = sw.widget(i)
                        on = ""
                        try:
                            on = w.objectName().lower()
                        except Exception:
                            pass
                        if on and ("unit" in on or "page_unit" in on or "chapter" in on):
                            target_index = i
                            break
            except Exception:
                pass
            try:
                self.ui.stackedWidget.setCurrentIndex(target_index)
            except Exception:
                pass
            print(f"DEBUG: selected subject -> {self.selected_subject} (switched to page {target_index})")
        except Exception as e:
            print("on_subject_clicked error:", e)

    def debug_print_stacked_pages(self):
        try:
            sw = getattr(self.ui, "stackedWidget", None)
            if sw is None:
                print("debug_print_stacked_pages: no stackedWidget found")
                return
            cnt = sw.count()
            print("DEBUG stackedWidget page count:", cnt)
            for i in range(cnt):
                w = sw.widget(i)
                oname = ""
                try:
                    oname = w.objectName()
                except Exception:
                    pass
                print(f"  index={i}, widget_class={w.__class__.__name__ if w else '<None>'}, objectName={oname}")
        except Exception as e:
            print("debug_print_stacked_pages failed:", e)

    def _row_to_dict_safe(self, r):
        try:
            if r is None:
                return {}
            if isinstance(r, dict):
                return r
            if hasattr(r, "keys"):
                return {k: r[k] for k in r.keys()}
            return dict(r)
        except Exception:
            try:
                return dict(r)
            except Exception:
                return {}

    # ---------- wrong-list UI / practice ----------
    def refresh_wrong_list(self, limit: int = None):
        try:
            if limit is None:
                limit = getattr(self, "max_questions", None)
            try:
                if limit is not None:
                    limit = int(limit)
            except Exception:
                limit = getattr(self, "max_questions", None)

            raw = db.get_wrong_questions_for_user(self.user_id, limit=limit)
            if raw is None:
                raw = []

            norm = []
            for r in raw:
                d = self._row_to_dict_safe(r)
                if 'qtype' in d and not d.get('type'):
                    d['type'] = d.get('qtype')
                norm.append(d)

            self._cached_wrongs = norm

            try:
                self.ui.listWidget_wrong.clear()
            except Exception:
                pass
            for q in norm:
                qid = q.get('id') or q.get('qid') or q.get('question_id') or ""
                stem = q.get('stem') or q.get('q_stem') or ""
                label = f"{qid}. {stem[:60]}" if qid else stem[:60]
                try:
                    self.ui.listWidget_wrong.addItem(label)
                except Exception:
                    pass

            try:
                if self.ui.listWidget_wrong.count() > 0:
                    self.ui.listWidget_wrong.setCurrentRow(0)
            except Exception:
                pass

            print(f"refresh_wrong_list: loaded {len(norm)} items (limit={limit})")
        except Exception as e:
            print("refresh_wrong_list error:", e)
            self._cached_wrongs = getattr(self, "_cached_wrongs", [])

    def on_wrong_item_changed(self, row):
        try:
            wrongs = getattr(self, "_cached_wrongs", None)
            if wrongs is None:
                raw = db.get_wrong_questions_for_user(self.user_id)
                wrongs = [self._row_to_dict_safe(r) for r in (raw or [])]
                self._cached_wrongs = wrongs

            if row is None or row < 0 or row >= len(wrongs):
                if hasattr(self.ui, "textEdit_2"):
                    self.ui.textEdit_2.clear()
                return

            q = wrongs[row]
            stem = q.get('stem') or q.get('q_stem') or ""
            opts = q.get('options') or []
            ans = q.get('answer') or []
            analysis = q.get('analysis') or ""
            html = "<b>题目：</b><br/>" + stem + "<br/><br/>"
            if opts:
                if isinstance(opts, (list, tuple)):
                    html += "<b>选项：</b><br/>" + "<br/>".join(opts) + "<br/><br/>"
                else:
                    html += "<b>选项：</b><br/>" + str(opts) + "<br/><br/>"
            html += "<b>答案：</b> " + (", ".join(ans) if isinstance(ans, (list, tuple)) else str(ans)) + "<br/><br/>"
            html += "<b>解析：</b><br/>" + analysis

            if hasattr(self.ui, "textEdit_2"):
                self.ui.textEdit_2.setHtml(html)
            else:
                QMessageBox.information(self, "错题详情", html)
        except Exception as e:
            print("on_wrong_item_changed error:", e)

    def start_wrong_practice(self, limit: int = None, shuffle: bool = False):
        try:
            wrongs = db.get_wrong_questions_for_user(self.user_id, limit=limit or self.max_questions)
        except Exception as e:
            logging.exception("Failed to load wrong questions")
            QMessageBox.critical(self, "错误", f"加载错题本失败：{e}")
            return

        if not wrongs:
            QMessageBox.information(self, "提示", "你的错题本为空。")
            return

        if shuffle:
            try:
                random.shuffle(wrongs)
            except Exception:
                pass

        lim = int(limit) if limit and int(limit) > 0 else self.max_questions
        if len(wrongs) > lim:
            wrongs = wrongs[:lim]

        normalized = []
        for q in wrongs:
            normalized.append({
                "id": q.get("id"),
                "subject": q.get("subject"),
                "unit": q.get("unit"),
                "stem": q.get("stem") or "",
                "type": (q.get("type") or q.get("qtype") or "single"),
                "options": q.get("options") if isinstance(q.get("options"), (list, tuple)) else (
                            q.get("options") or []),
                "answer": q.get("answer") if isinstance(q.get("answer"), (list, tuple)) else (q.get("answer") or []),
                "analysis": q.get("analysis") or ""
            })

        self.questions = normalized
        self.cur_index = 0
        self.finished = False
        self.in_wrong_mode = True

        practice_page_index = 4
        sw = getattr(self.ui, "stackedWidget", None)
        if sw is not None:
            for i in range(sw.count()):
                try:
                    on = sw.widget(i).objectName().lower()
                except Exception:
                    on = ""
                if on and ("practice" in on or "page_practice" in on or "page_practice1" in on):
                    practice_page_index = i
                    break

        try:
            self.ui.stackedWidget.setCurrentIndex(practice_page_index)
            QApplication.processEvents()
        except Exception:
            pass

        try:
            self._bind_practice_nav_buttons(practice_page_index)
        except Exception:
            pass

        print(f"DEBUG start_wrong_practice: loaded {len(self.questions)} wrong questions, practice_page={practice_page_index}")

        self.show_question(0)
        self._update_nav_buttons_state()

    # ---------- practice / question rendering ----------
    def start_practice(self, unit: int = None, subject: str = None, shuffle: bool = False):
        try:
            use_subject = subject if subject is not None else self.selected_subject
            if use_subject is None:
                QMessageBox.information(self, "提示", "请先选择科目")
                return

            use_unit = None
            if unit is not None:
                try:
                    use_unit = int(unit)
                except Exception:
                    use_unit = unit

            try:
                filtered = db.load_questions_filtered(subject=use_subject, unit=use_unit)
            except Exception as e:
                logging.exception("DB load failed in start_practice")
                QMessageBox.critical(self, "错误", f"加载题库失败：{e}")
                return

            if not filtered:
                QMessageBox.information(self, "提示", "本单元暂无题目，请先导入或选择其他单元")
                return

            if shuffle:
                random.shuffle(filtered)

            maxq = getattr(self, "max_questions", 10)
            if maxq <= 0:
                maxq = 10
            if len(filtered) > maxq:
                filtered = filtered[:maxq]

            self.questions = filtered
            self.cur_index = 0
            self.finished = False
            self.in_wrong_mode = False

            # bind nav buttons for practice page as well
            try:
                # attempt to find practice page index
                practice_page_index = 4
                sw = getattr(self.ui, "stackedWidget", None)
                if sw is not None:
                    for i in range(sw.count()):
                        try:
                            on = sw.widget(i).objectName().lower()
                        except Exception:
                            on = ""
                        if on and ("practice" in on or "page_practice" in on or "page_practice1" in on):
                            practice_page_index = i
                            break
                self._bind_practice_nav_buttons(practice_page_index)
            except Exception:
                pass

            self.show_question(0)
            self._update_nav_buttons_state()
        except Exception as e:
            logging.exception("start_practice unhandled")
            QMessageBox.critical(self, "错误", f"开始练习失败（已记录）：{e}")

    def _normalize_options(self, raw):
        if raw is None:
            return []
        if isinstance(raw, (list, tuple)):
            return [str(x) for x in raw]
        if isinstance(raw, dict):
            return [str(v) for v in raw.values()]
        if isinstance(raw, str):
            s = raw.strip()
            if not s:
                return []
            try:
                parsed = json.loads(s)
                if isinstance(parsed, (list, tuple)):
                    return [str(x) for x in parsed]
                if isinstance(parsed, dict):
                    return [str(v) for v in parsed.values()]
            except Exception:
                pass
            for sep in ["\n", "||", "|", ";", "；", ","]:
                if sep in s:
                    parts = [p.strip() for p in s.split(sep) if p.strip()]
                    if parts:
                        return parts
            return [s]
        return [str(raw)]

    def show_question(self, index: int):
        """Render question at index on the current practice page (robust)."""
        try:
            print(f"\n*** ENTER show_question(index={index}) ***")
            if not hasattr(self, "questions") or not self.questions:
                print("show_question: no questions loaded")
                if hasattr(self.ui, "label_3"):
                    self.ui.label_3.setText("题库为空，请导入题目或检查 sample_questions.json")
                return

            total = len(self.questions)
            print("show_question: total questions in memory =", total)
            if index < 0:
                index = 0
            if index >= total:
                print("show_question: index out of range -> switching to finish page")
                try:
                    self.ui.stackedWidget.setCurrentIndex(self.ui.stackedWidget.count() - 1)
                except Exception:
                    pass
                return

            self.cur_index = index
            q = self.questions[index]
            self.current_q = q
            qid = q.get("id", "<no-id>")
            stem = q.get("stem", "") or ""
            raw_opts = q.get("options", None)
            print("show_question: now showing index:", index, " id:", qid)
            print("show_question: stem preview ->", repr(stem[:200]))

            opts = self._normalize_options(raw_opts)
            print("show_question: normalized options ->", opts)

            # hide answer areas until submit
            try:
                if hasattr(self.ui, "textEdit_answer"):
                    self.ui.textEdit_answer.setVisible(False)
                if hasattr(self.ui, "textEdit_answer2"):
                    self.ui.textEdit_answer2.setVisible(False)
                if hasattr(self.ui, "textEdit_answer3"):
                    self.ui.textEdit_answer3.setVisible(False)
            except Exception:
                pass

            page_map = {
                4: (getattr(self.ui, "frame_12", None), "verticalLayout_7", getattr(self.ui, "label_3", None)),
                5: (getattr(self.ui, "frame_14", None), "verticalLayout_9", getattr(self.ui, "label_5", None)),
                6: (getattr(self.ui, "frame_16", None), "verticalLayout_12", getattr(self.ui, "label_8", None)),
            }

            try:
                cur_page = self.ui.stackedWidget.currentIndex()
            except Exception:
                cur_page = 4
            target_page = cur_page if cur_page in page_map else 4

            page_frame, layout_attr, page_label = page_map.get(target_page, (getattr(self.ui, "frame_12", None), "verticalLayout_7", getattr(self.ui, "label_3", None)))
            try:
                if page_label is not None:
                    page_label.setText(stem)
            except Exception:
                pass

            # remove existing container for this page
            try:
                if target_page in self.options_containers:
                    old_cont = self.options_containers.pop(target_page)
                    if hasattr(old_cont, "_layout"):
                        for i in reversed(range(old_cont._layout.count())):
                            item = old_cont._layout.itemAt(i)
                            if item:
                                w = item.widget()
                                if w:
                                    try:
                                        old_cont._layout.removeWidget(w)
                                        w.setParent(None)
                                        w.deleteLater()
                                    except Exception:
                                        pass
                    try:
                        old_cont.setParent(None)
                        old_cont.deleteLater()
                    except Exception:
                        pass
            except Exception:
                pass

            static_radio_names = ["radioButton", "radioButton_2", "radioButton_3", "radioButton_4",
                                  "radioButton_9", "radioButton_10", "radioButton_11", "radioButton_12"]
            for name in static_radio_names:
                try:
                    r = getattr(self.ui, name, None)
                    if r is not None:
                        r.hide()
                        try:
                            r.setChecked(False)
                        except Exception:
                            pass
                except Exception:
                    pass

            try:
                if getattr(self, "option_button_group", None) is not None:
                    old_bg = self.option_button_group
                    try:
                        for b in list(old_bg.buttons()):
                            try:
                                old_bg.removeButton(b)
                            except Exception:
                                pass
                    except Exception:
                        pass
            except Exception:
                pass
            self.option_button_group = None

            cont = QtWidgets.QWidget(parent=page_frame)
            cont.setObjectName(f"opts_container_p{target_page}")
            cont.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
            lay = QtWidgets.QVBoxLayout(cont)
            lay.setContentsMargins(0, 0, 0, 0)
            cont._layout = lay

            try:
                if hasattr(self.ui, layout_attr):
                    page_layout = getattr(self.ui, layout_attr)
                    try:
                        if page_layout.indexOf(cont) == -1:
                            page_layout.insertWidget(1, cont)
                    except Exception:
                        try:
                            page_layout.addWidget(cont)
                        except Exception:
                            cont.setParent(page_frame)
                else:
                    cont.setParent(page_frame)
            except Exception:
                cont.setParent(page_frame)

            self.current_option_widgets = []
            self.current_options_page = target_page
            qtype = (q.get("type") or "single").lower()

            def has_leading_letter(s):
                return bool(re.match(r'^\s*[A-Za-z]\s*[\.\、\)]', str(s).strip()))

            if qtype == "single":
                try:
                    bg = QtWidgets.QButtonGroup(cont)
                    bg.setExclusive(True)
                    self.option_button_group = bg
                except Exception:
                    bg = None
                    self.option_button_group = None

                if not opts:
                    lbl = QtWidgets.QLabel("（本题暂无选项 — 可能为主观题或选项格式有误）", parent=cont)
                    cont._layout.addWidget(lbl)
                    self.current_option_widgets.append(lbl)
                else:
                    for i, opt in enumerate(opts):
                        rb = QtWidgets.QRadioButton(parent=cont)
                        text = opt
                        if has_leading_letter(text):
                            rb.setText(text)
                        else:
                            rb.setText(f"{chr(ord('A') + i)}. {text}")
                        rb.letter = chr(ord('A') + i)
                        cont._layout.addWidget(rb)
                        rb.show()
                        self.current_option_widgets.append(rb)
                        if bg is not None:
                            try:
                                bg.addButton(rb, i)
                            except Exception:
                                pass

            elif qtype == "multi":
                self.option_button_group = None
                if not opts:
                    lbl = QtWidgets.QLabel("（本题暂无选项 — 可能为主观题或选项格式有误）", parent=cont)
                    cont._layout.addWidget(lbl)
                    self.current_option_widgets.append(lbl)
                else:
                    for i, opt in enumerate(opts):
                        cb = QtWidgets.QCheckBox(parent=cont)
                        text = opt
                        if has_leading_letter(text):
                            cb.setText(text)
                        else:
                            cb.setText(f"{chr(ord('A') + i)}. {text}")
                        cb.letter = chr(ord('A') + i)
                        cont._layout.addWidget(cb)
                        cb.show()
                        self.current_option_widgets.append(cb)

            elif qtype == "text":
                te = QtWidgets.QTextEdit(parent=cont)
                te.setFixedHeight(140)
                cont._layout.addWidget(te)
                te.show()
                self.current_option_widgets = [te]
                self.option_button_group = None

            else:
                lbl = QtWidgets.QLabel("未知题型或题目数据格式错误", parent=cont)
                cont._layout.addWidget(lbl)
                lbl.show()
                self.current_option_widgets = [lbl]
                self.option_button_group = None

            self.options_containers[target_page] = cont

            try:
                self.ui.stackedWidget.setCurrentIndex(target_page)
                QtWidgets.QApplication.processEvents()
            except Exception:
                pass

            print(f"CREATED {len(self.current_option_widgets)} option widgets; qid={qid}; qtype={qtype}")
            # *** 关键改动：每次渲染后更新按钮状态，确保“最后一题”Next 保持可点击 ***
            try:
                self._update_nav_buttons_state()
            except Exception:
                pass

            print("*** EXIT show_question normally ***\n")
        except Exception as e:
            print("show_question: UNHANDLED EXCEPTION ->", e)
            traceback.print_exc()

    def next_question(self, step=1):
        try:
            if not hasattr(self, "questions") or not self.questions:
                print("DEBUG next_question: no questions loaded")
                return

            total = len(self.questions)
            print(f"DEBUG next_question called: cur_index={self.cur_index}, step={step}, total={total}")
            new_index = self.cur_index + step
            if new_index < 0:
                new_index = 0

            if new_index >= total:
                # end -> go to finish page
                self.cur_index = total
                self.finished = True
                finish_index = self.ui.stackedWidget.count() - 1
                try:
                    self.ui.stackedWidget.setCurrentIndex(finish_index)
                except Exception:
                    pass
                # keep next disabled after finish
                for name in ("pushButton_next1", "pushButton_next2", "pushButton_next3"):
                    if hasattr(self.ui, name):
                        try:
                            getattr(self.ui, name).setEnabled(False)
                        except Exception:
                            pass
                print("DEBUG next_question: reached end -> switched to finish page")
                return

            # set and render
            self.cur_index = new_index
            self.show_question(self.cur_index)
            # after rendering, update nav state
            self._update_nav_buttons_state()
        except Exception as e:
            logging.exception("next_question unhandled error")
            QMessageBox.critical(self, "错误", f"翻页时发生错误（已记录）：{e}")

    # ---------- submit (保持你现有逻辑，只调用了 refresh_wrong_list(limit=...)) ----------
    def submit_current_answer(self):
        try:
            q = getattr(self, "current_q", None)
            if q is None:
                QMessageBox.information(self, "提示", "当前没有题目")
                return

            widgets = getattr(self, "current_option_widgets", None)
            if not widgets:
                page = getattr(self, "current_options_page", None)
                if page and page in self.options_containers:
                    cont = self.options_containers[page]
                    widgets = []
                    try:
                        layout = cont._layout
                        for i in range(layout.count()):
                            item = layout.itemAt(i)
                            if item:
                                w = item.widget()
                                if w:
                                    widgets.append(w)
                    except Exception:
                        widgets = None

            if not widgets:
                QMessageBox.warning(self, "提示", "未检测到选项控件（内部错误或题目无选项）")
                print("DEBUG submit: no widgets - current_option_widgets:", getattr(self, "current_option_widgets", None))
                return

            selected = []
            correct_flag = False
            qtype = (q.get("type") or "single").lower()

            if qtype == "single":
                chosen_letter = None
                if getattr(self, "option_button_group", None):
                    try:
                        chk = self.option_button_group.checkedButton()
                        if chk is not None:
                            chosen_letter = getattr(chk, "letter", None)
                            if not chosen_letter:
                                txt = chk.text().strip() if hasattr(chk, "text") else ""
                                m = re.match(r'\s*([A-Za-z])', txt)
                                if m:
                                    chosen_letter = m.group(1).upper()
                                else:
                                    chosen_letter = txt
                    except Exception:
                        pass

                if not chosen_letter:
                    found = False
                    for w in widgets:
                        if hasattr(w, "isChecked") and callable(w.isChecked) and w.isChecked():
                            found = True
                            chosen_letter = getattr(w, "letter", None)
                            if not chosen_letter:
                                txt = w.text().strip() if hasattr(w, "text") else ""
                                m = re.match(r'\s*([A-Za-z])', txt)
                                if m:
                                    chosen_letter = m.group(1).upper()
                                else:
                                    chosen_letter = txt
                            break
                    if not found:
                        QMessageBox.warning(self, "提示", "请先选择一个选项")
                        return

                selected = [chosen_letter] if chosen_letter else []
                normalized_sel = [s.strip().upper() for s in selected if s]
                normalized_ans = [a.strip().upper() for a in (q.get("answer") or [])]
                if normalized_ans and normalized_sel and normalized_sel[0] in normalized_ans:
                    correct_flag = True
                else:
                    correct_flag = False

            elif qtype == "multi":
                sel_letters = []
                for w in widgets:
                    if hasattr(w, "isChecked") and callable(w.isChecked) and w.isChecked():
                        letter = getattr(w, "letter", None)
                        if not letter:
                            txt = w.text().strip() if hasattr(w, "text") else ""
                            m = re.match(r'\s*([A-Za-z])', txt)
                            letter = m.group(1).upper() if m else txt
                        sel_letters.append(letter)
                if not sel_letters:
                    QMessageBox.warning(self, "提示", "请先勾选至少一个选项")
                    return
                selected = sel_letters
                normalized_sel = set([s.strip().upper() for s in selected if s])
                normalized_ans = set([a.strip().upper() for a in (q.get("answer") or [])])
                correct_flag = (len(normalized_ans) > 0 and normalized_sel == normalized_ans)

            elif qtype == "text":
                te = None
                for w in widgets:
                    if isinstance(w, QtWidgets.QTextEdit):
                        te = w
                        break
                if te is None:
                    QMessageBox.warning(self, "提示", "请先输入答案")
                    return
                user_text = te.toPlainText().strip()
                if not user_text:
                    QMessageBox.warning(self, "提示", "请先输入答案")
                    return
                selected = [user_text]
                correct_flag = False

            try:
                db.record_user_answer(self.user_id, q['id'], selected, correct_flag)
                self.refresh_wrong_list(limit=self.max_questions)
            except Exception as e:
                QMessageBox.critical(self, "记录失败", str(e))
                return

            ans_list = q.get("answer") or []
            ans_html = "<b>答案：</b> " + (", ".join(ans_list) if isinstance(ans_list, (list,tuple)) else str(ans_list)) + "<br/><br>"
            ans_html += "<b>解析：</b><br/>" + (q.get("analysis") or "无解析")

            page_for_ans = getattr(self, "current_options_page", None)
            if page_for_ans is None:
                try:
                    page_for_ans = self.ui.stackedWidget.currentIndex()
                except Exception:
                    page_for_ans = 4

            ans_widget = None
            if page_for_ans == 4 and hasattr(self.ui, "textEdit_answer"):
                ans_widget = self.ui.textEdit_answer
            elif page_for_ans == 5 and hasattr(self.ui, "textEdit_answer2"):
                ans_widget = self.ui.textEdit_answer2
            elif page_for_ans == 6 and hasattr(self.ui, "textEdit_answer3"):
                ans_widget = self.ui.textEdit_answer3
            else:
                for name in ("textEdit_answer", "textEdit_answer2", "textEdit_answer3"):
                    if hasattr(self.ui, name):
                        ans_widget = getattr(self.ui, name)
                        break

            if ans_widget is None:
                QMessageBox.information(self, "提交完成", "已记录答案（但未找到答题解析显示区域）")
            else:
                try:
                    ans_widget.setHtml(ans_html)
                    ans_widget.setVisible(True)
                    try:
                        vbar = ans_widget.verticalScrollBar()
                        if vbar:
                            vbar.setValue(0)
                    except Exception:
                        pass
                except Exception:
                    QMessageBox.information(self, "答案", ans_html)

            self.update_statistics_display()
            print("DEBUG submit: selected =", selected, " correct_flag =", correct_flag)
        except Exception as e:
            traceback.print_exc()
            QMessageBox.critical(self, "错误", f"提交答案时发生内部错误：{e}")

    def update_statistics_display(self):
        try:
            stats = db.get_user_stats(self.user_id)
            total = stats.get('total', 0) if isinstance(stats, dict) else 0
            correct = stats.get('correct', 0) if isinstance(stats, dict) else 0
            acc = stats.get('accuracy', 0.0) if isinstance(stats, dict) else 0.0
            self.ui.label_total_count.setText(f"<html><body><p>总刷题数</p><p style='font-size:18pt; font-weight:bold;'>{total}</p></body></html>")
            self.ui.label_accuracy_rate.setText(f"<html><body><p>正确率</p><p style='font-size:18pt; font-weight:bold;'>{acc:.1f}%</p></body></html>")
            wrongs = db.get_wrong_questions_for_user(self.user_id)
            self.ui.label_wrong_count.setText(f"<html><body><p>错题数</p><p style='font-size:18pt; font-weight:bold;'>{len(wrongs)}</p></body></html>")
            self.ui.label_time_count.setText(f"<html><body><p>学习时长</p><p style='font-size:18pt; font-weight:bold;'>--</p></body></html>")
        except Exception as e:
            print("update_statistics_display error:", e)

    # ---------- small utilities ----------
    def logout(self):
        self.close()
        QApplication.quit()

    def choose_file(self):
        path, _ = QFileDialog.getOpenFileName(self, "选择题库文件", "", "JSON 文件 (*.json);;文本文件 (*.txt)")
        if path:
            try:
                self.ui.lineEdit.setText(path)
            except Exception:
                pass

    def confirm_import(self):
        """
        替换你原来的 confirm_import，支持 .json（原行为）和 .txt（解析后导入）。
        依赖 db.import_questions_from_list 或 db.import_questions_from_json_file。
        """
        path = self.ui.lineEdit.text().strip() if hasattr(self.ui, "lineEdit") else ""
        if not path:
            QMessageBox.warning(self, "提示", "请先选择文件")
            return
        try:
            if path.lower().endswith(".json"):
                n = db.import_questions_from_json_file(path)
                QMessageBox.information(self, "导入完成", f"已导入 {n} 道题（追加）")
            elif path.lower().endswith(".txt"):
                # parse txt into list of questions
                parsed = parse_txt_questions(path)
                if not parsed:
                    QMessageBox.warning(self, "导入失败", "解析后未发现题目，请检查 TXT 格式")
                    return
                # call db.import_questions_from_list (返回值 may not exist -> we will count)
                try:
                    # try to use import_questions_from_list if available
                    if hasattr(db, "import_questions_from_list"):
                        db.import_questions_from_list(parsed)
                        n = len(parsed)
                    else:
                        # fallback: write a temp json and reuse import_questions_from_json_file
                        import tempfile, json
                        tf = tempfile.NamedTemporaryFile(delete=False, suffix=".json", mode="w", encoding="utf-8")
                        json.dump(parsed, tf, ensure_ascii=False, indent=2)
                        tf.close()
                        n = db.import_questions_from_json_file(tf.name)
                        try:
                            os.unlink(tf.name)
                        except Exception:
                            pass
                    QMessageBox.information(self, "导入完成", f"已导入 {n} 道题（追加）")
                except Exception as e:
                    QMessageBox.critical(self, "导入失败", f"解析成功但导入数据库失败：{e}")
                    return
            else:
                QMessageBox.warning(self, "不支持格式",
                                    "当前仅支持 JSON 或 TXT 导入（你可以把题库转为 sample_questions.json 格式）")
                return

            # reload and update UI
            self.questions = db.load_questions()
            try:
                self.update_statistics_display()
            except Exception:
                pass
        except Exception as e:
            QMessageBox.critical(self, "导入失败", str(e))




def main():
    app = QtWidgets.QApplication(sys.argv)
    
    # 确保数据库中有一个默认用户
    username = "default_user"
    password = "123456"
    user = db.get_user(username)
    if not user:
        # 创建默认用户
        salt, h = utils.hash_password(password)
        db.add_user(username, salt, h)
        user = db.get_user(username)
    
    user_id, username, _, _ = user
    
    # 直接创建主窗口
    win = MainWindow(user_id, username)
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
