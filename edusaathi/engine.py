"""Question bank loading, student model and adaptive sequencing."""
import json
from pathlib import Path
from .mastery import BKTParams, update

DATA = Path(__file__).resolve().parent.parent / "data" / "question_bank.json"
MASTERY_THRESHOLD = 0.85
PREREQ_MIN = 0.60

def load_bank(path: Path = DATA) -> dict:
    with open(path, encoding="utf-8") as fh:
        bank = json.load(fh)
    ids = [q["id"] for q in bank["questions"]]
    if len(ids) != len(set(ids)):
        raise ValueError("Duplicate question ids in the bank")
    for q in bank["questions"]:
        if q["topic"] not in bank["topics"] or not 0 <= q["answer"] < len(q["options"]):
            raise ValueError(f"Invalid question {q['id']}")
    return bank

class Student:
    def __init__(self, bank: dict, prm: BKTParams = BKTParams()):
        self.bank, self.prm = bank, prm
        self.mastery = {t: prm.p_init for t in bank["topics"]}
        self.asked = []
        self.log = []

    def record(self, q: dict, correct: bool) -> None:
        self.asked.append(q["id"])
        self.log.append((q["id"], correct))
        self.mastery[q["topic"]] = update(self.mastery[q["topic"]], correct, self.prm)

    def diagnostic(self) -> list:
        """One easiest question per topic, in bank order."""
        out = []
        for t in self.bank["topics"]:
            qs = sorted((q for q in self.bank["questions"] if q["topic"] == t), key=lambda q: q["difficulty"])
            if qs:
                out.append(qs[0])
        return out

    def _eligible(self, t: str) -> bool:
        return all(self.mastery[p] >= PREREQ_MIN for p in self.bank["topics"][t]["prereq"])

    def next_question(self):
        """Pick the weakest unmastered topic whose prerequisites are met; difficulty follows mastery."""
        cands = [t for t in self.bank["topics"] if self.mastery[t] < MASTERY_THRESHOLD and self._eligible(t)]
        for t in sorted(cands, key=lambda x: self.mastery[x]):
            want = 1 if self.mastery[t] < 0.40 else 2 if self.mastery[t] < 0.70 else 3
            pool = [q for q in self.bank["questions"] if q["topic"] == t and q["id"] not in self.asked]
            if pool:
                return min(pool, key=lambda q: (abs(q["difficulty"] - want), q["id"]))
        return None

    def done(self) -> bool:
        return all(m >= MASTERY_THRESHOLD for m in self.mastery.values())

    def report(self) -> list:
        return sorted(self.mastery.items(), key=lambda kv: kv[1])
