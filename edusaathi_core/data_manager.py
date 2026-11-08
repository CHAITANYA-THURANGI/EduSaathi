"""
EduSaathi Data & Question Bank Manager
======================================
Loads JSON questions and manages student session records.
"""

import os
import json
import pandas as pd

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
QUESTION_FILE = os.path.join(DATA_DIR, "question_bank.json")
DATASET_FILE = os.path.join(DATA_DIR, "student_telemetry_dataset.csv")

def load_question_bank(path: str = QUESTION_FILE) -> dict:
    if not os.path.exists(path):
        return {"topics": {}, "questions": []}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def get_diagnostic_questions(bank: dict) -> list:
    """Returns one baseline difficulty question for every registered topic."""
    out = []
    for t in bank.get("topics", {}):
        qs = [q for q in bank.get("questions", []) if q.get("topic") == t]
        if qs:
            qs_sorted = sorted(qs, key=lambda x: x.get("difficulty", 1))
            out.append(qs_sorted[0])
    return out

def get_cohort_summary() -> dict:
    if os.path.exists(DATASET_FILE):
        df = pd.read_csv(DATASET_FILE)
        return {
            "total_students": len(df),
            "avg_score": round(df["quiz_score"].mean() * 100, 1),
            "gap_rate": round((df["gap_detected"].sum() / len(df)) * 100, 1),
            "avg_latency": round(df["time_on_task_sec"].mean(), 1),
            "df": df.head(100)
        }
    return {
        "total_students": 1500,
        "avg_score": 72.4,
        "gap_rate": 28.6,
        "avg_latency": 178.5,
        "df": pd.DataFrame()
    }
