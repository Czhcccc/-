# _*_ coding : utf-8 _*_
# @Time : 2025/11/12 18:39
# @Author : Star_And_Kiss
# @File : main
# @Project : PythonProject1

"""
刷题软件主程序入口
包含登录窗口和主窗口的类定义和业务逻辑
"""

import os
import sys

# 将本地lib目录添加到Python模块搜索路径
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib"))

# 设置Qt平台插件路径
try:
    import PyQt5
    pyqt5_dir = os.path.dirname(PyQt5.__file__)
    qt5_path = os.path.join(pyqt5_dir, "Qt5")
    platforms_path = os.path.join(qt5_path, "plugins", "platforms")
    if os.path.exists(platforms_path):
        os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = platforms_path
        print(f"设置Qt平台插件路径: {platforms_path}")
    else:
        print(f"Qt平台插件路径不存在: {platforms_path}")
except ImportError as e:
    print(f"无法导入PyQt5: {e}")
    print(f"Python模块搜索路径: {sys.path}")

from LoginUi import *
from InterfaceUi import *
from PyQt5 import QtCore  # 导入QtCore模块
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect  # 补充阴影类

# 全局变量：存储当前登录用户信息
user_now = ''  # 当前用户


class LogWindow(QMainWindow):
    """登录窗口类，处理用户登录和注册功能"""

    def __init__(self):
        super().__init__()
        # 初始化UI界面
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)

        # 设置窗口无边框和透明背景
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # 添加阴影效果
        self.shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        self.shadow.setOffset(5, 5)
        self.shadow.setBlurRadius(10)
        self.shadow.setColor(QtCore.Qt.gray)
        self.ui.frame.setGraphicsEffect(self.shadow)

        # 连接登录和注册按钮的页面切换
        self.ui.pushButton_Login.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentIndex(0))
        self.ui.pushButton_Register.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentIndex(1))

        # 连接登录确认按钮
        self.ui.button_L_sure.clicked.connect(self.login_in)

        # 设置输入框样式
        input_style = """
        QLineEdit{
            background-color: rgba(255, 255, 255, 0);
            border: none;
            border-bottom: 1px solid #ccc;
            padding: 5px;
        }
        QLineEdit:focus{
            border-bottom: 2px solid #ff9900;
            color: #333;
        }
        QLineEdit:placeholder-text{
            color: #999;
        }
        """
        self.ui.line_L_account.setStyleSheet(input_style)
        self.ui.line_L_password.setStyleSheet(input_style)
        self.ui.lineEdit_R_account.setStyleSheet(input_style)
        self.ui.lineEdit_R_password1.setStyleSheet(input_style)
        self.ui.lineEdit_R_password2.setStyleSheet(input_style)

        # 密码可见性切换（添加按钮）
        self.show_pwd_btn = QtWidgets.QPushButton(self.ui.Login)
        self.show_pwd_btn.setGeometry(QtCore.QRect(260, 40, 20, 20))
        self.show_pwd_btn.setText("👁")
        self.show_pwd_btn.setStyleSheet("border: none; background: transparent;")
        self.show_pwd_btn.clicked.connect(self.toggle_pwd_visibility)
        self.show()

    def toggle_pwd_visibility(self):
        """切换密码显示/隐藏状态"""
        current_mode = self.ui.line_L_password.echoMode()
        if current_mode == QtWidgets.QLineEdit.Password:
            self.ui.line_L_password.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.show_pwd_btn.setText("🙈")
        else:
            self.ui.line_L_password.setEchoMode(QtWidgets.QLineEdit.Password)
            self.show_pwd_btn.setText("👁")

    def login_in(self):
        """处理用户登录逻辑"""
        account = self.ui.line_L_account.text()
        password = self.ui.line_L_password.text()

        # TODO: 这里需要后端人员替换为真实的数据库验证
        # 当前使用硬编码测试账号：123/123456
        if account == "123" and password == "123456":
            # 登录成功，打开主窗口并关闭登录窗口
            self.win = MainWindow()
            self.close()
        else:
            # 登录失败，提示错误信息
            print("密码错误")  # TODO: 可以替换为更友好的弹窗提示


class MainWindow(QMainWindow):
    """主窗口类，包含刷题软件的所有主要功能"""

    def __init__(self):
        super().__init__()
        # 初始化UI界面
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 设置窗口无边框和透明背景
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # 添加阴影效果
        self.shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        self.shadow.setOffset(5, 5)
        self.shadow.setBlurRadius(10)
        self.shadow.setColor(QtCore.Qt.gray)
        self.ui.frame_7.setGraphicsEffect(self.shadow)

        # 默认隐藏刷题页面的答案部分
        self.ui.textEdit_answer.setVisible(False)
        self.ui.textEdit_answer2.setVisible(False)
        self.ui.textEdit_answer3.setVisible(False)

        # ==================== 页面切换连接 ====================

        # 主菜单导航
        self.ui.pushButton_home.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.pushButton_my.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.pushButton_module.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(3))

        # 科目选择（都跳转到单元选择页面）
        self.ui.pushButton_Mao.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.pushButton_MAX.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.pushButton_Outline.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.pushButton_Moral.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.pushButton_Xi.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))

        # 退出登录
        self.ui.pushButton_logout.clicked.connect(self.logout)

        # 单元选择（章节按钮）
        self.ui.pushButton_fir.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(4))
        self.ui.pushButton_sec.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(4))
        self.ui.pushButton_thi.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(4))
        self.ui.pushButton_fou.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(4))
        self.ui.pushButton_fif.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(4))
        self.ui.pushButton_six.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(4))
        self.ui.pushButton_sev.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(4))
        self.ui.pushButton_eig.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(4))
        self.ui.pushButton_nin.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(4))
        self.ui.pushButton_ten.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(4))

        # 刷题页面导航
        self.ui.pushButton_next1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(5))
        self.ui.pushButton_next2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(6))
        self.ui.pushButton_next3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(7))
        self.ui.pushButton_last2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(4))
        self.ui.pushButton_last3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(5))

        # 功能模块页面切换
        self.ui.pushButton_wrong.clicked.connect(lambda: self.ui.stackedWidget_3.setCurrentIndex(3))
        self.ui.pushButton_import.clicked.connect(lambda: self.ui.stackedWidget_3.setCurrentIndex(1))
        self.ui.pushButton_statistics.clicked.connect(lambda: self.ui.stackedWidget_3.setCurrentIndex(2))

        # 返回按钮连接
        self.ui.pushButton_wrong_return.clicked.connect(lambda: self.ui.stackedWidget_3.setCurrentIndex(0))
        self.ui.pushButton_import_return.clicked.connect(lambda: self.ui.stackedWidget_3.setCurrentIndex(0))
        self.ui.pushButton_finish_return.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.pushButton_statistics_return.clicked.connect(lambda: self.ui.stackedWidget_3.setCurrentIndex(0))

        # 显示答案按钮
        self.ui.pushButton_show_answer1.clicked.connect(lambda: self.ui.textEdit_answer.setVisible(True))
        self.ui.pushButton_show_answer2.clicked.connect(lambda: self.ui.textEdit_answer2.setVisible(True))
        self.ui.pushButton_show_answer3.clicked.connect(lambda: self.ui.textEdit_answer3.setVisible(True))

        # 错题本列表与内容联动
        self.ui.listWidget_wrong.currentRowChanged.connect(self.on_wrong_item_changed)

        # 初始化统计数据
        self.init_statistics_data()

        self.show()

    def logout(self):
        """处理用户退出登录"""
        self.close()
        self.login = LogWindow()
        user_now = ''  # 清空当前用户信息

    def on_wrong_item_changed(self, row):
        """当错题本列表项改变时，切换右侧显示的内容"""
        if row >= 0:  # 确保有选中的项
            self.ui.stackedWidget_wrong.setCurrentIndex(row)

    def init_statistics_data(self):
        """
        初始化统计数据
        TODO: 后端人员需要替换为从数据库获取真实数据
        """
        # 模拟数据 - 需要后端替换为真实数据查询
        self.total_questions = 156  # 总刷题数
        self.correct_questions = 122  # 正确题目数
        self.wrong_questions = 34  # 错题数
        self.study_time = "12.5h"  # 学习时长

        # 更新显示
        self.update_statistics_display()

    def update_statistics_display(self):
        """更新统计数据显示"""
        # 计算正确率
        accuracy = (self.correct_questions / self.total_questions) * 100 if self.total_questions > 0 else 0

        # 更新左侧数据卡片（使用富文本格式显示）
        self.ui.label_total_count.setText(
            f"<html><head/><body><p>总刷题数</p><p style=\"font-size:18pt; font-weight:bold;\">{self.total_questions}</p></body></html>")
        self.ui.label_accuracy_rate.setText(
            f"<html><head/><body><p>正确率</p><p style=\"font-size:18pt; font-weight:bold;\">{accuracy:.1f}%</p></body></html>")
        self.ui.label_wrong_count.setText(
            f"<html><head/><body><p>错题数</p><p style=\"font-size:18pt; font-weight:bold;\">{self.wrong_questions}</p></body></html>")
        self.ui.label_time_count.setText(
            f"<html><head/><body><p>学习时长</p><p style=\"font-size:18pt; font-weight:bold;\">{self.study_time}</p></body></html>")

    def show_statistics_page(self):
        """显示数据统计页面并更新数据"""
        self.update_statistics_display()
        self.ui.stackedWidget_3.setCurrentIndex(2)  # 切换到统计页面


if __name__ == '__main__':
    # 创建QApplication实例
    app = QApplication(sys.argv)

    # 创建并显示登录窗口
    win = LogWindow()

    # 进入主事件循环
    sys.exit(app.exec_())