# 🧠 EduSaathi: Pedagogical & AI Architecture Specification

## 1. Problem Formulation: The Rural Learning Crisis & Bloom's 2-Sigma Problem
In rural educational ecosystems, learners in multi-grade classrooms frequently accumulate compounding conceptual deficits. When a foundational arithmetic prerequisite (such as fractional parts of a whole) is left unmastered, higher-order mathematical competencies (decimals, ratios, percentages, algebraic equations) become unreachable.

In 1984, educational psychologist **Benjamin Bloom** demonstrated that one-to-one mastery tutoring elevates student achievement by two standard deviations (the **2-Sigma Problem**) compared to conventional lecture-based classrooms. EduSaathi algorithmically operationalizes this personalized mastery tutoring loop on low-cost edge hardware.

---

## 2. Dual-Engine Probabilistic & Machine Learning Modeling

### A. Bayesian Knowledge Tracing (Corbett & Anderson, 1994)
EduSaathi models student knowledge as a latent binary state for each curriculum competency $k$:
- $L_t = 1$: Concept is mastered.
- $L_t = 0$: Concept is unmastered.

#### 4-Parameter Formulation:
1. **Prior Knowledge Probability $P(L_0) = 0.30$**: Baseline likelihood that a rural learner has acquired the concept before testing.
2. **Knowledge Transition Probability $P(T) = 0.15$**: Likelihood of transitioning from unmastered to mastered state following an instructional opportunity.
3. **Slip Probability $P(S) = 0.10$**: Probability that a student who genuinely knows the concept makes a careless error.
4. **Guess Probability $P(G) = 0.25$**: Probability that an unmastered student guesses correctly on a 4-choice item.

#### Posterior Update Equations:
Following an observation at opportunity $t$:

$$\text{If Correct: } P(L_t \mid \text{Obs} = 1) = \frac{P(L_t)(1 - P(S))}{P(L_t)(1 - P(S)) + (1 - P(L_t))P(G)}$$

$$\text{If Incorrect: } P(L_t \mid \text{Obs} = 0) = \frac{P(L_t)P(S)}{P(L_t)P(S) + (1 - P(L_t))(1 - P(G))}$$

#### Learning Update:
$$P(L_{t+1}) = P(L_t \mid \text{Obs}) + (1 - P(L_t \mid \text{Obs})) \cdot P(T)$$

A competency is designated **Mastered** when $P(L_t) \ge 0.85$.

---

### B. Supervised Random Forest Telemetry Classifier
To distinguish genuine conceptual deficits from accidental misclicks or speed variations, EduSaathi extracts an interaction telemetry vector:

$$\mathbf{x} = [\text{quiz\_score}, \text{time\_on\_task\_sec}, \text{retry\_count}, \text{hint\_used}, \text{previous\_mastery}, \text{difficulty\_avg}]$$

- **Model Architecture:** 100 decorrelated decision trees (`max_depth=6`, `min_samples_split=4`).
- **Target:** Binary classification ($\text{gap\_detected} \in \{0, 1\}$).
- **Inference Latency:** $< 15$ ms on edge devices.

---

## 3. Prerequisite Directed Acyclic Graph (DAG) Sequencing
Topics are represented as nodes in a Directed Acyclic Graph $G = (V, E)$, where directed edges $(u, v) \in E$ indicate that competency $u$ is a strict prerequisite for competency $v$.

```
    [ Fractions ]
       /     \
      v       v
 [ Decimals ] [ Ratio & Proportion ]
      \       /
       v     v
    [ Percentages ]
```
And:
```
 [ Fractions ] ────────> [ Simple Equations ]
```

### Sequencing Invariants:
1. **Prerequisite Gate:** Topic $v$ cannot be assigned unless:
   $$\forall u \in \text{Prereqs}(v), \quad P(L_u) \ge 0.60$$
2. **Remediation Priority:** Among eligible unmastered topics ($P(L_t) < 0.85$), the engine selects the node with the lowest current mastery and highest topological priority.

---

## 4. Offline-First Micro-Architecture
- **Local Storage:** SQLite embedded relational storage caching question banks, telemetry vectors, and student mastery maps.
- **Zero Network Overhead:** The entire assessment and BKT loop runs with 0 KB internet bandwidth consumption.
- **Asynchronous Sync:** When connection is detected, telemetry diffs are compressed (< 20 KB per student) and transmitted to the central education cloud.
