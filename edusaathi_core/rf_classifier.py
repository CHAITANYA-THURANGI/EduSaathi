"""
EduSaathi Supervised Telemetry Classifier (Random Forest)
=========================================================
Trains and serves an ensemble of 100 decorrelated decision trees
to predict whether a student interaction signals a genuine conceptual gap.
"""

import os
import joblib
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

MODEL_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "gap_detector.pkl")

def generate_telemetry_dataset(n_samples=1500, random_state=42):
    np.random.seed(random_state)
    quiz_scores = np.random.beta(a=2.5, b=2.0, size=n_samples)
    time_on_task = np.clip(np.random.normal(loc=180, scale=60, size=n_samples), 30, 600)
    retry_count = np.clip(np.random.poisson(lam=1.2, size=n_samples), 0, 5)
    hint_used = np.random.binomial(n=1, p=0.35, size=n_samples)
    previous_mastery = np.random.uniform(0.3, 0.95, size=n_samples)
    difficulty_avg = np.random.choice([1.0, 1.8, 2.5], size=n_samples, p=[0.4, 0.4, 0.2])
    
    latent_risk = (
        (1.0 - quiz_scores) * 0.55 +
        (retry_count / 5.0) * 0.20 +
        (time_on_task / 600.0) * 0.15 +
        hint_used * 0.10 - (previous_mastery * 0.20)
    )
    gap_prob = 1 / (1 + np.exp(-(latent_risk - 0.45) * 10))
    gap_detected = (gap_prob + np.random.normal(0, 0.05, size=n_samples) > 0.5).astype(int)
    
    return pd.DataFrame({
        "quiz_score": np.round(quiz_scores, 2),
        "time_on_task_sec": np.round(time_on_task, 1),
        "retry_count": retry_count,
        "hint_used": hint_used,
        "previous_mastery": np.round(previous_mastery, 2),
        "difficulty_avg": difficulty_avg,
        "gap_detected": gap_detected
    })

def train_gap_model():
    df = generate_telemetry_dataset()
    data_path = os.path.join(os.path.dirname(__file__), "..", "data", "student_telemetry_dataset.csv")
    df.to_csv(data_path, index=False)
    
    X = df[["quiz_score", "time_on_task_sec", "retry_count", "hint_used", "previous_mastery", "difficulty_avg"]]
    y = df["gap_detected"]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    
    rf = RandomForestClassifier(n_estimators=100, max_depth=6, min_samples_split=4, random_state=42)
    rf.fit(X_train, y_train)
    
    preds = rf.predict(X_test)
    metrics = {
        "accuracy": accuracy_score(y_test, preds),
        "precision": precision_score(y_test, preds),
        "recall": recall_score(y_test, preds),
        "f1": f1_score(y_test, preds),
        "confusion_matrix": confusion_matrix(y_test, preds).tolist()
    }
    joblib.dump(rf, MODEL_FILE)
    return rf, metrics

def predict_gap(features: list):
    """
    Evaluates telemetry vector: [score, time_sec, retries, hints, prev_mastery, difficulty]
    """
    if os.path.exists(MODEL_FILE):
        rf = joblib.load(MODEL_FILE)
    else:
        rf, _ = train_gap_model()
        
    vec = np.array(features).reshape(1, -1)
    prediction = int(rf.predict(vec)[0])
    prob = float(rf.predict_proba(vec)[0][1])
    return prediction, prob
