# EduSaathi: Complete Project Implementation & Execution Guide

**Project Title:** EduSaathi — An AI-Powered Personalized Learning Companion for Rural Students  
**Course Code:** 22ADI02 — Industrial Internship / Rural Internship  
**Department:** Department of Artificial Intelligence & Data Science, CBIT Hyderabad  
**Target Environment:** Windows 10/11, Python 3.10+ (Recommended: Python 3.11/3.12)  

---

## 📁 1. Project Directory Structure

Inside the `EduSaathi_Software_Suite` folder (or extracted from `10_Project_Source_Code.zip`), you will find the following clean modular architecture:

```
EduSaathi_Software_Suite/
│
├── config.py                       # Global project constants, theme colors, 22ADI02 metadata
├── app_streamlit.py                # Main interactive Streamlit application (Student & Teacher modes)
├── requirements.txt                # Python package dependencies
├── run_web.bat                     # 1-click batch launcher for Streamlit web interface
├── run_cli_tests.bat               # 1-click batch launcher for automated unit testing
│
├── edusaathi_core/                 # Core AI & Pedagogical Engine
│   ├── __init__.py                 # Package initializer
│   ├── bkt_mastery.py              # Bayesian Knowledge Tracing probabilistic updater
│   ├── rf_classifier.py            # Random Forest gap detector & synthetic telemetry trainer
│   ├── recommendation_engine.py    # Prerequisite DAG & trilingual remedial sequencer
│   └── data_manager.py             # Trilingual question loader & cohort analytics engine
│
├── data/                           # Data Assets
│   ├── question_bank.json          # Trilingual questions across 5 math topics (EN, HI, TE)
│   └── gap_detector.pkl            # Pre-trained serialized Random Forest model (100 trees)
│
└── tests/                          # Automated Unit Test Suite
    ├── __init__.py                 # Test package initializer
    └── test_edusaathi.py           # 8 automated unit tests verifying all core algorithms
```

---

## ⚙️ 2. Prerequisites & Environment Setup

### Step 2.1: Verify Python Installation
Open **Command Prompt (cmd)** or **PowerShell** and verify that Python 3.10 or higher is installed:

```powershell
python --version
```
*Expected Output:* `Python 3.10.x` or `Python 3.11.x` or `Python 3.12.x`.

If Python is not installed or not recognized, download and install the official Windows installer from [python.org](https://www.python.org/downloads/), ensuring you check the box **"Add Python to PATH"**.

---

### Step 2.2: Navigate to Project Directory
In your terminal, navigate to the folder:

```powershell
cd "c:\Users\chait\OneDrive - Chaitanya Bharathi Institute of Technology\CHAITANYA\Internship\IBM_summer_internship\EduSaathi_Ultimate_Submission\EduSaathi_Software_Suite"
```

---

### Step 2.3: Install Required Dependencies
Run the standard pip install command:

```powershell
pip install -r requirements.txt
```

The dependencies specified in `requirements.txt` are:
```
streamlit>=1.30.0
scikit-learn>=1.3.0
pandas>=2.0.0
numpy>=1.24.0
joblib>=1.3.0
```
*Note: EduSaathi uses standard lightweight libraries that run on any standard CPU without requiring GPU acceleration or proprietary software.*

---

## 🚀 3. How to Run the Application

### Option A: The 1-Click Batch File (Easiest)
Simply double-click the file **`run_web.bat`** in Windows File Explorer.  
Alternatively, run it from your command line:

```powershell
.\run_web.bat
```

This will automatically start the local Streamlit server and open your default web browser to:
`http://localhost:8501`

---

### Option B: Running via Streamlit CLI Directly
If you prefer running directly in terminal or VS Code:

```powershell
python -m streamlit run app_streamlit.py
```

---

## 🧪 4. How to Run Automated Unit Tests

EduSaathi includes a comprehensive automated test suite in `tests/test_edusaathi.py` that verifies the mathematical soundness of BKT, Random Forest predictions, prerequisite graph logic, and multilingual question schemas.

### Option A: The 1-Click Test Launcher
Double-click **`run_cli_tests.bat`** or execute:

```powershell
.\run_cli_tests.bat
```

---

### Option B: Executing unittest Directly
Run:

```powershell
python -m unittest discover -s tests -v
```

### Expected Output:
```
test_bkt_correct_response_increases_mastery (test_edusaathi.TestEduSaathiSuite) ... ok
test_bkt_incorrect_response_decreases_mastery (test_edusaathi.TestEduSaathiSuite) ... ok
test_bkt_initialization (test_edusaathi.TestEduSaathiSuite) ... ok
test_cohort_analytics_computation (test_edusaathi.TestEduSaathiSuite) ... ok
test_prerequisite_eligibility_rule (test_edusaathi.TestEduSaathiSuite) ... ok
test_question_bank_integrity (test_edusaathi.TestEduSaathiSuite) ... ok
test_rf_classifier_prediction_structure (test_edusaathi.TestEduSaathiSuite) ... ok
test_rf_classifier_training_and_accuracy (test_edusaathi.TestEduSaathiSuite) ... ok

----------------------------------------------------------------------
Ran 8 tests in 0.216s

OK
```

---

## 🖥️ 5. Step-by-Step Live Demonstration Guide

When demonstrating EduSaathi to faculty or evaluators, follow these exact 4 steps:

### Step 1: Language & Topic Selection
1. In the sidebar, select your preferred language: **English**, **తెలుగు (Telugu)**, or **हिन्दी (Hindi)**.
2. Select a topic, such as **Fractions and Decimals** or **Linear Equations in One Variable**.
3. Point out that the entire user interface and math formulas seamlessly switch to the chosen regional language.

### Step 2: Diagnostic Assessment Interaction
1. Click **"Start Diagnostic Quiz"**.
2. Answer the micro-diagnostic questions.
3. Notice that EduSaathi's telemetry engine tracks your **active answering duration (seconds)**, **retries**, and whether you request a **Hint**.
4. Click **"Submit Assessment"**.

### Step 3: AI Diagnostic Gap Analysis & BKT Mastery
1. EduSaathi immediately computes and displays your results:
   - **Score Percentage**
   - **BKT Latent Mastery Probability $P(L_t)$** (e.g., 0.88 - Mastery Achieved)
   - **Random Forest Gap Classification** (e.g., `Proficient` or `Learning Gap Detected`)
2. Show that if you took an unusually long time or used multiple retries, the Random Forest model flags the interaction for foundational reinforcement even if your score was decent.
3. Point to the personalized remedial pathway sequenced by the **Prerequisite DAG**.

### Step 4: Educator Analytics Dashboard
1. In the sidebar navigation, switch from **Student Assessment** to **Teacher Dashboard**.
2. Show the cohort-level overview:
   - Total Students Assessed
   - Class Average Score
   - Overall Gap Incidence Rate
   - Topic-by-topic weakness distribution chart
3. Explain that this dashboard grants village teachers immediate diagnostic visibility into which foundational concepts need whole-classroom review.

---

## 🔧 6. Troubleshooting Common Issues

| Issue | Root Cause | Solution |
|:---|:---|:---|
| `'streamlit' is not recognized` | Streamlit package not in PATH | Run `python -m pip install streamlit` or invoke via `python -m streamlit run app_streamlit.py` |
| Port 8501 already in use | Previous Streamlit instance still running | Run on alternative port: `python -m streamlit run app_streamlit.py --server.port 8502` |
| `FileNotFoundError: question_bank.json` | Running python from outside project root | Ensure terminal working directory is `EduSaathi_Software_Suite/` before launching |
| Missing model `gap_detector.pkl` | Model file was moved or deleted | Run `python -c "from edusaathi_core.rf_classifier import RFGapClassifier; RFGapClassifier().train()"` to instantly retrain and save a fresh model |
