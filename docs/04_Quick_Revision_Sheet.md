# EduSaathi: Last-Minute Rapid Revision & Viva Defense Sheet

> [!TIP]
> **READ THIS 5 MINUTES BEFORE YOUR PRESENTATION & VIVA VOCE.**  
> Keep these numbers, definitions, and one-liners at the top of your mind.

---

## ⚡ The Essential 30-Second Elevator Pitch
> *"EduSaathi is an offline-first, trilingual AI learning companion for rural school students. Because rural classrooms have high 40:1 student-teacher ratios, foundational concept gaps compound silently. EduSaathi logs student telemetry (time, retries, scores) during diagnostic quizzes, uses a 100-tree Random Forest classifier to detect conceptual gaps with 95.33% accuracy, and sequences localized remedial lessons in Telugu, Hindi, and English—directly advancing UN SDG 4: Quality Education."*

---

## 📊 Essential Numbers to Memorize

| Metric / Parameter | Value to State | Explanation |
|:---|:---:|:---|
| **Model Classification Accuracy** | **95.33%** | Evaluated on held-out 20% test split (300 samples) |
| **Precision (Gap Class)** | **78.57%** | When AI flags a gap, it is 78.6% certain to be real |
| **Recall (Gap Class)** | **50.00%** | Catches half of latent gaps in initial micro-quiz |
| **F1-Score** | **61.11%** | Harmonic mean balancing precision and recall |
| **Inference Latency** | **$<$ 15 ms** | Sub-15 millisecond execution on standard CPU |
| **Model Memory Footprint** | **285 KB** | Extremely lightweight; runs on cheap mobile devices |
| **Ensemble Tree Count** | **100 Trees** | `n_estimators=100`, `max_depth=6` |
| **Telemetry Dataset Size** | **1,500 records** | Simulated rural student telemetry interactions |
| **Student-Teacher Ratio** | **$>$ 40:1** | Real-world problem in rural government schools |
| **Regional Content Deficit** | **$<$ 10%** | Of commercial EdTech is available in regional languages |
| **Internship Hours** | **20 Hours** | 8 modules completed, verified under AICTE / IBM SkillsBuild |
| **Course Code & Credits** | **22ADI02** | 2 Credits, 50 Marks CIE (Industrial/Rural Internship) |

---

## 🧩 The 6 Telemetry Signals in Our Feature Vector
1. `quiz_score` (0.0 to 1.0) — **49.14%** importance (dominant indicator).
2. `retry_count` (0 to 5) — **13.21%** importance (hesitation & struggle).
3. `hint_used` (0 or 1) — **12.74%** importance (conscious lack of self-efficacy).
4. `previous_mastery` (0.0 to 1.0) — **12.13%** importance (baseline history).
5. `time_on_task_sec` (30 to 600s) — **10.18%** importance (cognitive processing latency).
6. `difficulty_avg` (1.0 to 3.0) — **2.59%** importance (curriculum weight normalization).

---

## 🏛️ The 4 Architecture Layers
1. **Student Interface Tier:** Streamlit Web UI + future WhatsApp bot; supports English, Telugu, and Hindi.
2. **Application Layer:** Manages session state, quiz timer, and trilingual translation mappings.
3. **AI/ML Inference Layer:** Scikit-Learn Random Forest model (`gap_detector.pkl`) + Prerequisite Recommendation Engine.
4. **Cloud & Data Layer:** Local JSON/CSV offline cache + asynchronous IBM Cloud synchronization.

---

## ⚠️ What NEVER to Say in the Viva

| ❌ NEVER Say This: | ✅ INSTEAD Say This: |
|:---|:---|
| *"We used Deep Learning and LLMs to detect the gaps."* | *"We used a Scikit-Learn **Random Forest Classifier** because tabular telemetry runs in <15ms on low-cost CPUs without needing a GPU."* |
| *"We collected data from 1,500 real students in our village."* | *"We generated a **statistically calibrated synthetic telemetry dataset of 1,500 records** based on published educational data mining research."* |
| *"ChatGPT wrote our entire project code."* | *"We utilized AI developer tools for **syntax acceleration and pair programming**, while designing the architecture, models, and code logic ourselves."* |
| *"This is just an internship presentation."* | *"This is an engineering prototype fulfilling **Course Code 22ADI02**, applying IBM SkillsBuild AI training to solve rural educational inequity."* |

---

## 🎯 Rapid 1-Liner Answers to Sudden Questions

- **"Who is your mentor?"** $\rightarrow$ *Mrs. Swathi Tejah Yalla, Assistant Professor, Department of AI&DS.*
- **"Who is your coordinator?"** $\rightarrow$ *Mrs. V. Vasuki Rohinidevi, Assistant Professor, Department of AI&DS.*
- **"Who is your Head of Department?"** $\rightarrow$ *Dr. K. Radhika, Professor & Head, Department of AI&DS.*
- **"Why did you use Random Forest?"** $\rightarrow$ *High accuracy (95.33%), low variance, sub-15ms edge inference, and zero GPU requirement.*
- **"How does offline mode work?"** $\rightarrow$ *All questions, models, and remedial texts are stored locally in JSON and pickle format.*
- **"What does the teacher see?"** $\rightarrow$ *Cohort-level gap rates, average class scores, and topic failure frequencies.*
- **"How to launch the app?"** $\rightarrow$ `python -m streamlit run app_streamlit.py` (or double-click `run.bat`).
