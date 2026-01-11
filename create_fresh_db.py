# create_fresh_db.py
import os, shutil, time, json
from db import DB_PATH, ensure_tables, import_questions_from_json_file

def backup_old_db():
    if os.path.exists(DB_PATH):
        t = time.strftime("%Y%m%d_%H%M%S")
        bak = f"{DB_PATH}.bak_{t}"
        shutil.move(DB_PATH, bak)
        print(f"Existing DB moved to: {bak}")
    else:
        print("No existing DB file found; creating new one.")

def create_new_db(import_sample=True):
    print("Creating new database...")
    ensure_tables()
    print("Empty DB (canonical schema) created.")
    if import_sample:
        sample = "sample_questions.json"
        if os.path.exists(sample):
            n = import_questions_from_json_file(sample)
            print(f"Imported {n} questions from {sample}.")
        else:
            print("No sample_questions.json found; skipping sample import.")
    # print summary
    try:
        from db import load_questions
        qs = load_questions(limit=5)
        print(f"Sample of questions (first 5): {len(qs)} loaded.")
    except Exception:
        pass
    print("Done.")

if __name__ == "__main__":
    print("== Fresh DB Creator ==")
    ans = input("This will back up existing app_data.db (if exists) and create a fresh one. Continue? [y/N]: ").strip().lower()
    if ans != "y":
        print("Aborted.")
    else:
        backup_old_db()
        create_new_db(import_sample=True)
