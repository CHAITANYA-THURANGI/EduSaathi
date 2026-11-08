# 🎓 EduSaathi: Comprehensive Technical Viva & Defense Guide

## Core Engineering & Pedagogical Concepts

### Q1. Why use Bayesian Knowledge Tracing (BKT) instead of a simple percentage average?
**Answer:** A simple percentage score cannot distinguish between a student who answered correctly by guessing (lucky 25% chance) and one who truly understands. Conversely, a wrong answer can occur due to a careless slip rather than lack of knowledge. BKT mathematically isolates slips $P(S)$ and guesses $P(G)$ from true latent knowledge $P(L_t)$, providing an accurate probabilistic assessment.

### Q2. What are the four parameters of BKT and how were their default values selected?
**Answer:** Following Corbett & Anderson (1994):
- $P(L_0) = 0.30$: Initial probability of prior knowledge in rural baseline cohorts.
- $P(T) = 0.15$: Probability of learning/transitioning on each instructional encounter.
- $P(S) = 0.10$: Slip rate (error despite knowing).
- $P(G) = 0.25$: Guess rate (1 out of 4 multiple-choice options).

### Q3. Why use a Directed Acyclic Graph (DAG) for curriculum sequencing?
**Answer:** Mathematics is inherently hierarchical. Learning *Percentages* without understanding *Decimals* and *Ratio & Proportion* creates cognitive overload. The DAG models curriculum dependencies as directed edges, mathematically preventing circular prerequisites and guaranteeing that foundational concepts are solidified before advanced topics are assigned.

### Q4. How does the Random Forest Telemetry Classifier enhance the system?
**Answer:** The Random Forest model evaluates continuous interaction velocity: response duration (seconds), retry frequency, hint usage, prior mastery, and difficulty level. An ensemble of 100 decorrelated decision trees analyzes these multivariate features to flag genuine conceptual gaps ($\ge 0.50$ probability) that raw scores alone might miss.

### Q5. How does EduSaathi function in rural schools with zero internet?
**Answer:** EduSaathi operates an offline-first architecture. The question bank, BKT engine, Random Forest inference model, and interaction logger run 100% locally on the device (Python standard library / local Python runtime). When connectivity is intermittently available, batched encrypted telemetry is pushed asynchronously.

### Q6. What is the computational complexity of the sequencing algorithm?
**Answer:** 
- Prerequisite validation: $O(|V| + |E|)$ topological traversal across the 5 curriculum nodes.
- Next question selection: $O(N)$ filter where $N \le 20$ questions in the pool.
- Total execution time is under 15 milliseconds, suitable for low-cost ARM processors (Raspberry Pi 3/4, low-spec Android tablets).
