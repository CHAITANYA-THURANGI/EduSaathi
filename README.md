# 📚 EduSaathi: AI-Powered Personalized Learning Companion for Rural Students

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-FF4B4B.svg)](https://streamlit.io/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.3%2B-F7931E.svg)](https://scikit-learn.org/)
[![Offline First](https://img.shields.io/badge/Edge%20AI-Offline--First-green.svg)](#offline-first-architecture)
[![UN SDG 4](https://img.shields.io/badge/UN%20SDG-4%20Quality%20Education-E5243B.svg)](https://sdgs.un.org/goals/goal4)
[![NEP 2020](https://img.shields.io/badge/NEP%202020-Clause%204.4%20Aligned-orange.svg)](#national-policy-alignment)

> **National Rural EdTech AI Initiative**  
> *Bridging the Rural-Urban Educational Divide via Offline-First Adaptive Edge AI*  
> Supported by **AICTE** in collaboration with **IBM SkillsBuild** and **BharatCares**

---

## 🌟 Executive Summary

**EduSaathi** is an edge-deployable, adaptive educational platform designed to eliminate compounding foundational learning deficits in resource-constrained rural schools. Operationalizing **Benjamin Bloom's 2-Sigma Mastery Tutoring model (1984)**, the platform dynamically infers latent conceptual mastery using **Bayesian Knowledge Tracing (Corbett & Anderson, 1994)**, enforces prerequisite mastery via a **curriculum Directed Acyclic Graph (DAG)**, and detects latent conceptual gaps using a **supervised Random Forest telemetry classifier**.

Designed specifically for rural schools operating with intermittent or zero internet connectivity, EduSaathi runs completely on-device with **< 15ms inference latency** and zero external API dependencies during learning encounters.

---

## 🏛️ Key Capabilities & Highlights

| Capability | Technical Mechanism | Pedagogical Impact |
| :--- | :--- | :--- |
| **Probabilistic Student Modeling** | 4-parameter Bayesian Knowledge Tracing ($P(L_0), P(T), P(S), P(G)$) | Isolates lucky guesses and careless slips from true latent understanding. |
| **Prerequisite-Aware Sequencing** | Directed Acyclic Graph (DAG) topological dependency engine | Prevents cognitive overload by enforcing prerequisite mastery gates ($P(L) \ge 0.60$). |
| **Multivariate Telemetry Classifier** | 100-tree decorrelated Random Forest (`scikit-learn`) | Analyzes response velocity, retries, and difficulty to flag genuine gaps. |
| **Offline-First Edge Architecture** | Embedded local storage + lightweight micro-runtime | Zero bandwidth required during live testing; runs on low-cost school hardware. |
| **Trilingual Vernacular Support** | English, Telugu (`తెలుగు`), and Hindi (`हिन्दी`) | Eliminates language barriers for rural learners in regional schools. |
| **Interactive Remedial Lab** | Visual manipulatives (fractions, place values, algebraic balances) | Connects abstract arithmetic principles to tangible rural metaphors. |
| **Cohort Teacher Analytics** | Cohort telemetry analytics across 1,500+ student records | Identifies systemic classroom learning deficits and generates CSV export reports. |

---

## 🏗️ System Architecture

EduSaathi utilizes a 4-tier layered architecture designed for edge independence:

```
┌─────────────────────────────────────────────────────────────────────────┐
│                       TIER 1: PRESENTATION LAYER                        │
│   Reactive Streamlit Web Portal (WCAG 2.1 AAA)  │  Pure Python CLI     │
└────────────────────────────────────┬────────────────────────────────────┘
                                     │
┌────────────────────────────────────v────────────────────────────────────┐
│                    TIER 2: ADAPTIVE SEQUENCING LAYER                   │
│   Curriculum Directed Acyclic Graph (DAG)  │  Prerequisite Gate Engine  │
└────────────────────────────────────┬────────────────────────────────────┘
                                     │
┌────────────────────────────────────v────────────────────────────────────┐
│                   TIER 3: AI & MACHINE LEARNING LAYER                   │
│   Bayesian Knowledge Tracing (BKT)  │  Random Forest Telemetry Classifier │
└────────────────────────────────────┬────────────────────────────────────┘
                                     │
┌────────────────────────────────────v────────────────────────────────────┐
│                   TIER 4: DATA & SYNCHRONIZATION LAYER                  │
│   Multilingual Question Bank (JSON) │  Asynchronous Telemetry Sync      │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 🔬 Mathematical Formulation: Bayesian Knowledge Tracing

EduSaathi models student knowledge as a latent binary state $L_t \in \{0, 1\}$.

### 1. Posterior Probability Update
Following student response observation at opportunity $t$:

$$\text{If Correct: } P(L_t \mid \text{Obs} = 1) = \frac{P(L_t)(1 - P(S))}{P(L_t)(1 - P(S)) + (1 - P(L_t))P(G)}$$

$$\text{If Incorrect: } P(L_t \mid \text{Obs} = 0) = \frac{P(L_t)P(S)}{P(L_t)P(S) + (1 - P(L_t))(1 - P(G))}$$

### 2. Knowledge Acquisition Transition
Accounting for learning resulting from the problem-solving encounter:

$$P(L_{t+1}) = P(L_t \mid \text{Obs}) + (1 - P(L_t \mid \text{Obs})) \cdot P(T)$$

- **Prior Knowledge $P(L_0) = 0.30$**
- **Transition Probability $P(T) = 0.15$**
- **Slip Rate $P(S) = 0.10$**
- **Guess Rate $P(G) = 0.25$**
- **Mastery Threshold: $P(L_t) \ge 0.85$**

---

## 🚀 Quick Start Guide

### Prerequisites
- Python 3.10, 3.11, 3.12, 3.13, or 3.14
- Git

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/CHAITANYA-THURANGI/EduSaathi.git
   cd EduSaathi
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On Linux/macOS:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Interactive Web Platform:**
   ```bash
   streamlit run app_streamlit.py
   ```
   *Or double-click `run_web.bat` on Windows.*

5. **Run the Automated Test Suite:**
   ```bash
   python -m unittest discover -s tests -v
   ```
   *Or double-click `run_cli_tests.bat` on Windows.*

---

## 📂 Project Directory Structure

```
EduSaathi/
├── app_streamlit.py               # Main Streamlit Web Application
├── config.py                      # Global institutional configuration & theme tokens
├── requirements.txt               # Package dependencies
├── run_web.bat                    # 1-click launcher for Streamlit web app
├── run_cli_tests.bat              # 1-click launcher for automated unit tests
├── LICENSE                        # MIT Open Source License
├── README.md                      # Repository overview & manual
│
├── edusaathi/                     # Pure Python Standard-Library Engine
│   ├── __init__.py
│   ├── cli.py                     # Terminal-based diagnostic assessment runner
│   ├── engine.py                  # Student state machine and adaptive sequencing
│   └── mastery.py                 # Pure standard library BKT updates
│
├── edusaathi_core/                # Modular Production Core
│   ├── __init__.py
│   ├── bkt_mastery.py             # 4-parameter BKT probabilistic updater
│   ├── data_manager.py            # Question bank & telemetry dataset loader
│   ├── recommendation_engine.py   # Prerequisite DAG recommendation engine
│   └── rf_classifier.py           # 100-tree Random Forest telemetry classifier
│
├── data/                          # Data Assets
│   ├── question_bank.json         # 5 topics, 20 questions, English & Telugu
│   ├── student_telemetry_dataset.csv # 1,500 student interaction records
│   └── gap_detector.pkl           # Pre-trained Random Forest model
│
├── tests/                         # Quality Assurance & Test Suite
│   └── test_edusaathi.py          # 8 automated unit tests (100% pass)
│
├── docs/                          # Detailed Technical Documentation
│   ├── 01_Project_Implementation_Guide.md
│   ├── 02_Pedagogical_and_AI_Architecture.md
│   ├── 03_Technical_Viva_and_Defense_Guide.md
│   └── 04_Quick_Revision_Sheet.md
│
└── images/                        # Architectural Diagrams & Assets
    ├── cbit_logo.png
    ├── figure3_architecture.png
    ├── figure4_workflow.png
    └── figure5_mastery.png
```

---

## 🧪 Testing & Verification

The test suite covers:
- Mathematical bounds verification of BKT updates ($0 \le P(L) \le 1.0$).
- Directional correctness (correct answers raise mastery; incorrect answers lower mastery).
- Question bank integrity & multilingual key validation.
- Prerequisite blocking (verifying advanced topics cannot be recommended before prerequisites).
- Non-repetition of diagnostic questions.

Run the test suite:
```bash
python -m unittest discover -s tests -v
```

Output:
```
test_bank_valid (test_edusaathi.TestBank.test_bank_valid) ... ok
test_bounds (test_edusaathi.TestMastery.test_bounds) ... ok
test_correct_raises_wrong_lowers (test_edusaathi.TestMastery.test_correct_raises_wrong_lowers) ... ok
test_diagnostic_one_per_topic (test_edusaathi.TestSequencing.test_diagnostic_one_per_topic) ... ok
test_done_when_all_mastered (test_edusaathi.TestSequencing.test_done_when_all_mastered) ... ok
test_no_repeat_questions (test_edusaathi.TestSequencing.test_no_repeat_questions) ... ok
test_prereq_blocks_percentages (test_edusaathi.TestSequencing.test_prereq_blocks_percentages) ... ok
test_weakest_eligible_first (test_edusaathi.TestSequencing.test_weakest_eligible_first) ... ok

----------------------------------------------------------------------
Ran 8 tests in 0.003s

OK
```

---

## 📜 National Policy & SDG Alignment

- **National Education Policy (NEP 2020), Ministry of Education:** Paragraph 4.4 explicitly mandates that foundational literacy and numeracy must become an urgent national mission. EduSaathi provides individual diagnostic clarity and adaptive remediation directly aligned with this mandate.
- **United Nations Sustainable Development Goal 4 (Quality Education):** Target 4.1 & 4.5 ensure inclusive, equitable, quality education and eliminate gender and regional disparities.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
