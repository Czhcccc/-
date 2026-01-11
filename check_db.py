# inspect_wrong_book.py
import sqlite3, json, os

DB = "app_data.db"
if not os.path.exists(DB):
    print("DB not found:", DB)
    raise SystemExit(1)

conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row
cur = conn.cursor()


print("wrong_questions rows:")
cur.execute("SELECT * FROM wrong_questions ORDER BY id")
rows = cur.fetchall()
for r in rows:
    print(dict(r))

print("\nNow matching questions for each wrong_questions row:")
for r in rows:
    qid = None
    if "question_id" in r.keys() and r["question_id"] is not None:
        qid = r["question_id"]
    elif "qid" in r.keys() and r["qid"] is not None:
        qid = r["qid"]
    else:
        print("  row has no question id:", dict(r))
        continue
    cur.execute("SELECT id, stem, qtype, type, options, answer FROM questions WHERE id = ?", (qid,))
    q = cur.fetchone()
    if q:
        print(" matched:", dict(q))
    else:
        print(" no question found for qid=", qid)

conn.close()
