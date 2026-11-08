import unittest
from edusaathi.engine import Student, load_bank, MASTERY_THRESHOLD
from edusaathi.mastery import update

class TestMastery(unittest.TestCase):
    def test_correct_raises_wrong_lowers(self):
        self.assertGreater(update(0.5, True), 0.5)
        self.assertLess(update(0.5, False), update(0.5, True))
    def test_bounds(self):
        for p in (0.0, 0.3, 1.0):
            for c in (True, False):
                self.assertTrue(0.0 <= update(p, c) <= 1.0)

class TestBank(unittest.TestCase):
    def test_bank_valid(self):
        b = load_bank()
        self.assertEqual(len(b["questions"]), 20)
        self.assertEqual(set(b["ui"]["en"]), set(b["ui"]["te"]))

class TestSequencing(unittest.TestCase):
    def setUp(self): self.st = Student(load_bank())
    def test_diagnostic_one_per_topic(self):
        self.assertEqual(len(self.st.diagnostic()), 5)
    def test_prereq_blocks_percentages(self):
        self.st.mastery.update({"fractions": .1, "decimals": .2, "ratio": .2, "percentages": 0.0, "equations": .9})
        self.assertNotEqual(self.st.next_question()["topic"], "percentages")
    def test_weakest_eligible_first(self):
        self.st.mastery.update({"fractions": .9, "decimals": .5, "ratio": .3, "percentages": .1, "equations": .9})
        self.assertEqual(self.st.next_question()["topic"], "ratio")
    def test_no_repeat_questions(self):
        seen = set()
        while (q := self.st.next_question()) and len(seen) < 30:
            self.assertNotIn(q["id"], seen); seen.add(q["id"]); self.st.record(q, False)
    def test_done_when_all_mastered(self):
        for t in self.st.mastery: self.st.mastery[t] = MASTERY_THRESHOLD
        self.assertTrue(self.st.done()); self.assertIsNone(self.st.next_question())

if __name__ == "__main__":
    unittest.main()
