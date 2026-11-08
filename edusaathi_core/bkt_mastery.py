"""
EduSaathi Bayesian Knowledge Tracing (BKT) Engine
=================================================
Implements the standard 4-parameter probabilistic knowledge tracing model
(Corbett & Anderson, 1994) to track student concept mastery per topic.

Mathematical Formulations:
1. Prior probability of knowing concept t: P(L_t)
2. Evidence probability:
   If correct: P(C_t) = P(L_t)*(1 - P(S)) + (1 - P(L_t))*P(G)
   If wrong  : P(W_t) = P(L_t)*P(S) + (1 - P(L_t))*(1 - P(G))
3. Posterior probability:
   P(L_t | Answer) = P(L_t, Answer) / P(Answer)
4. Knowledge Transition Update:
   P(L_{t+1}) = P(L_t | Answer) + (1 - P(L_t | Answer)) * P(T)
"""

from dataclasses import dataclass

@dataclass(frozen=True)
class BKTParams:
    p_init: float = 0.30   # Prior probability the student already knows the topic
    p_learn: float = 0.15  # Transition probability of acquiring knowledge from an attempt
    p_slip: float = 0.10   # Slip probability: knowing the concept but answering incorrectly
    p_guess: float = 0.25  # Guess probability: answering correctly purely by chance (4 options)

def update_bkt(p_known: float, correct: bool, params: BKTParams = BKTParams()) -> float:
    """
    Computes updated probability of concept mastery following a student answer.
    """
    p_known = max(0.001, min(0.999, p_known))
    
    if correct:
        numerator = p_known * (1.0 - params.p_slip)
        denominator = numerator + (1.0 - p_known) * params.p_guess
    else:
        numerator = p_known * params.p_slip
        denominator = numerator + (1.0 - p_known) * (1.0 - params.p_guess)
        
    posterior = numerator / denominator if denominator > 0 else p_known
    # Add learning transition from the learning encounter
    new_mastery = posterior + (1.0 - posterior) * params.p_learn
    return round(float(max(0.0, min(1.0, new_mastery))), 4)
