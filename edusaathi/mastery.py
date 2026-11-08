"""Bayesian Knowledge Tracing (Corbett & Anderson, 1994) - one probability of mastery per topic."""
from dataclasses import dataclass

@dataclass(frozen=True)
class BKTParams:
    p_init: float = 0.30   # prior chance the student already knows the topic
    p_learn: float = 0.15  # chance of learning the topic after one attempt
    p_slip: float = 0.10   # chance of a wrong answer even though the topic is known
    p_guess: float = 0.25  # chance of a right answer when the topic is not known (4 options)

def update(p_known: float, correct: bool, prm: BKTParams = BKTParams()) -> float:
    """Return the new probability of mastery after one answer."""
    if correct:
        evidence = p_known * (1 - prm.p_slip) + (1 - p_known) * prm.p_guess
        posterior = p_known * (1 - prm.p_slip) / evidence
    else:
        evidence = p_known * prm.p_slip + (1 - p_known) * (1 - prm.p_guess)
        posterior = p_known * prm.p_slip / evidence
    return posterior + (1 - posterior) * prm.p_learn
