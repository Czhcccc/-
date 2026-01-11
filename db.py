# db.py -- HopeBox应用的标准SQLite数据库辅助模块
import sqlite3
import json
import os
import time
from typing import List, Dict, Any

DB_PATH = "app_data.db"

def _get_conn():
    # ensure directory exists
    d = os.path.dirname(DB_PATH)
    if d:
        os.makedirs(d, exist_ok=True)
    # longer timeout, allow cross-thread usage, WAL mode
    conn = sqlite3.connect(DB_PATH, timeout=30.0, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    try:
        conn.execute("PRAGMA journal_mode=WAL;")
        conn.execute("PRAGMA synchronous=NORMAL;")
        conn.execute("PRAGMA foreign_keys=ON;")
    except Exception:
        pass
    return conn

def _decode_list_field(field):
    if field is None:
        return []
    if isinstance(field, (list, tuple)):
        return [str(x) for x in field]
    s = str(field).strip()
    if not s:
        return []
    try:
        v = json.loads(s)
        if isinstance(v, (list, tuple)):
            return [str(x) for x in v]
        if isinstance(v, dict):
            return [str(x) for x in v.values()]
    except Exception:
        pass
    for sep in ["\n", "||", "|", ";", "；", ","]:
        if sep in s:
            parts = [p.strip() for p in s.split(sep) if p.strip()]
            if parts:
                return parts
    return [s]

def ensure_tables():
    """
    创建标准表结构。如果数据库存在旧版/遗留列，此函数将添加缺失的列，
    但不会尝试复杂的迁移操作。为了最简便的恢复，使用create_fresh_db.py创建新数据库。
    """
    conn = _get_conn()
    cur = conn.cursor()

    # 标准题库表
    cur.execute("""
    CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        subject TEXT,
        unit INTEGER,
        stem TEXT,
        qtype TEXT,
        options TEXT,
        answer TEXT,
        analysis TEXT,
        type TEXT
    )
    """)

    # 用户表
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        salt TEXT,
        pwd_hash TEXT,
        hash TEXT
    )
    """)

    # 用户答题记录（标准表）
    cur.execute("""
    CREATE TABLE IF NOT EXISTS user_answers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        question_id INTEGER,
        selected TEXT,
        correct INTEGER,
        ts INTEGER,
        timestamp TEXT
    )
    """)

    # 错题表（标准表）
    cur.execute("""
    CREATE TABLE IF NOT EXISTS wrong_questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        question_id INTEGER,
        added_at TEXT,
        UNIQUE(user_id, question_id)
    )
    """)

    conn.commit()
    conn.close()

# ---------------- 用户操作 ----------------
def add_user(username: str, salt_hex: str, hash_hex: str) -> bool:
    conn = _get_conn()
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO users (username, salt, pwd_hash) VALUES (?, ?, ?)",
                    (username, salt_hex, hash_hex))
        conn.commit()
        return True
    except Exception:
        return False
    finally:
        conn.close()

def get_user(username: str):
    conn = _get_conn()
    cur = conn.cursor()
    # 优先使用pwd_hash列
    cur.execute("SELECT id, username, salt, COALESCE(pwd_hash, hash) AS pwd_hash FROM users WHERE username = ?",
                (username,))
    row = cur.fetchone()
    conn.close()
    if not row:
        return None
    return (row["id"], row["username"], row["salt"], row["pwd_hash"])

# ---------------- 题目操作 ----------------
def import_questions_from_list(qs: List[Dict[str, Any]]):
    conn = _get_conn()
    cur = conn.cursor()
    for q in qs:
        opts = json.dumps(q.get("options") or [], ensure_ascii=False)
        ans = json.dumps(q.get("answer") or [], ensure_ascii=False)
        cur.execute("""
            INSERT INTO questions (subject, unit, stem, qtype, type, options, answer, analysis)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            q.get("subject"),
            q.get("unit"),
            q.get("stem"),
            q.get("type") or q.get("qtype"),
            q.get("type") or q.get("qtype"),
            opts,
            ans,
            q.get("analysis") or ""
        ))
    conn.commit()
    conn.close()

def import_questions_from_json_file(path: str):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    if isinstance(data, list):
        import_questions_from_list(data)
        return len(data)
    return 0

def load_questions(limit: int = None) -> List[Dict[str, Any]]:
    conn = _get_conn()
    cur = conn.cursor()
    sql = "SELECT id, subject, unit, stem, qtype, type, options, answer, analysis FROM questions ORDER BY id"
    if isinstance(limit, int) and limit > 0:
        sql += f" LIMIT {limit}"
    cur.execute(sql)
    rows = cur.fetchall()
    conn.close()
    res = []
    for r in rows:
        type_val = (r["type"] or r["qtype"]) if ("type" in r.keys() or "qtype" in r.keys()) else (r["qtype"] if "qtype" in r.keys() else None)
        res.append({
            "id": r["id"],
            "subject": r["subject"],
            "unit": r["unit"],
            "stem": r["stem"],
            "type": type_val or "single",
            "options": _decode_list_field(r["options"]),
            "answer": _decode_list_field(r["answer"]),
            "analysis": r["analysis"] or ""
        })
    return res

def load_questions_filtered(subject: str = None, unit: int = None, limit: int = None) -> List[Dict[str, Any]]:
    conn = _get_conn()
    cur = conn.cursor()
    clauses = []
    params = []
    if subject is not None:
        clauses.append("subject = ?"); params.append(subject)
    if unit is not None:
        clauses.append("unit = ?"); params.append(unit)
    sql = "SELECT id, subject, unit, stem, qtype, type, options, answer, analysis FROM questions"
    if clauses:
        sql += " WHERE " + " AND ".join(clauses)
    sql += " ORDER BY id"
    if isinstance(limit, int) and limit > 0:
        sql += f" LIMIT {limit}"
    cur.execute(sql, params)
    rows = cur.fetchall()
    conn.close()
    res = []
    for r in rows:
        type_val = (r["type"] or r["qtype"]) if ("type" in r.keys() or "qtype" in r.keys()) else (r["qtype"] if "qtype" in r.keys() else None)
        res.append({
            "id": r["id"],
            "subject": r["subject"],
            "unit": r["unit"],
            "stem": r["stem"],
            "type": type_val or "single",
            "options": _decode_list_field(r["options"]),
            "answer": _decode_list_field(r["answer"]),
            "analysis": r["analysis"] or ""
        })
    return res

# ---------------- 错题/统计 ----------------
def add_wrong_question(user_id: int, question_id: int):
    conn = _get_conn()
    try:
        cur = conn.cursor()
        ts = time.strftime("%Y-%m-%d %H:%M:%S")
        cur.execute("INSERT OR IGNORE INTO wrong_questions (user_id, question_id, added_at) VALUES (?, ?, ?)",
                    (user_id, question_id, ts))
        conn.commit()
    finally:
        conn.close()

def remove_wrong_question(user_id: int, question_id: int):
    conn = _get_conn()
    try:
        cur = conn.cursor()
        cur.execute("DELETE FROM wrong_questions WHERE user_id=? AND question_id=?", (user_id, question_id))
        conn.commit()
    finally:
        conn.close()

def get_wrong_questions_for_user(user_id: int, limit: int = None) -> List[Dict[str, Any]]:
    conn = _get_conn()
    try:
        cur = conn.cursor()
        sql = """
            SELECT q.* , w.id AS w_id
            FROM wrong_questions w
            JOIN questions q ON q.id = w.question_id
            WHERE w.user_id = ?
            ORDER BY w.id ASC
        """
        if isinstance(limit, int) and limit > 0:
            sql += f" LIMIT {limit}"
        cur.execute(sql, (user_id,))
        rows = cur.fetchall()
        res = []
        seen = set()
        for r in rows:
            qid = r["id"]
            if qid in seen:
                continue
            seen.add(qid)
            d = dict(r)
            d.pop("w_id", None)
            d["options"] = _decode_list_field(d.get("options"))
            d["answer"] = _decode_list_field(d.get("answer"))
            # prefer qtype if type empty
            if d.get("qtype") and not d.get("type"):
                d["type"] = d.get("qtype")
            res.append(d)
        return res
    finally:
        conn.close()

def get_user_stats(user_id: int):
    conn = _get_conn()
    cur = conn.cursor()
    try:
        cur.execute("SELECT COUNT(*) AS cnt, SUM(correct) AS s FROM user_answers WHERE user_id = ?", (user_id,))
        row = cur.fetchone()
        total = int(row["cnt"] or 0)
        correct = int(row["s"] or 0)
    except Exception:
        total = 0
        correct = 0
    conn.close()
    acc = (correct / total * 100) if total > 0 else 0.0
    return {"total": total, "correct": correct, "accuracy": acc}

def record_user_answer(user_id: int, question_id: int, selected, correct: bool, max_retries=6, base_delay=0.05):
    sel_json = json.dumps(selected, ensure_ascii=False)
    timestamp_str = time.strftime("%Y-%m-%d %H:%M:%S")
    ts = int(time.time())
    last_exc = None
    for attempt in range(max_retries):
        try:
            conn = _get_conn()
            cur = conn.cursor()
            cur.execute("INSERT INTO user_answers (user_id, question_id, selected, correct, ts, timestamp) VALUES (?, ?, ?, ?, ?, ?)",
                        (user_id, question_id, sel_json, 1 if correct else 0, ts, timestamp_str))
            conn.commit()
            conn.close()
            # update wrong list
            if correct:
                remove_wrong_question(user_id, question_id)
            else:
                add_wrong_question(user_id, question_id)
            return
        except sqlite3.OperationalError as e:
            last_exc = e
            if "locked" in str(e).lower():
                time.sleep(base_delay * (1 + attempt))
                continue
            else:
                raise
        except Exception:
            raise
    # if failed after retries, raise last exception
    raise last_exc
