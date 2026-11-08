"""Command line interface. Run:  python -m edusaathi.cli [--lang en|te] [--demo]"""
import argparse, random, sys
from .engine import Student, load_bank

def show_report(st, lang, ui):
    print(f"\n== {ui['path']} ==")
    for t, m in st.report():
        print(f"  {st.bank['topics'][t]['name'][lang]:<24} {m:5.2f}  {'#' * int(m * 20)}")

def run(lang="en", demo=False, max_q=25, seed=7, skill=None):
    bank = load_bank(); ui = bank["ui"][lang]; st = Student(bank)
    rng = random.Random(seed)
    skill = skill or {"fractions": .9, "decimals": .7, "ratio": .5, "percentages": .3, "equations": .8}
    queue = st.diagnostic()
    while len(st.asked) < max_q:
        q = queue.pop(0) if queue else st.next_question()
        if q is None:
            break
        print(f"\n[{bank['topics'][q['topic']]['name'][lang]} | level {q['difficulty']}] {q['text']}")
        for i, o in enumerate(q["options"]):
            print(f"  {'ABCD'[i]}. {o}")
        if demo:   # simulated learner (SYNTHETIC): right with probability = skill in that topic
            ok = rng.random() < skill[q["topic"]]
            print(f"  (simulated answer: {'correct' if ok else 'wrong'})")
        else:
            try:
                raw = input(ui["pick"]).strip().upper()
            except EOFError:
                break
            ok = len(raw) > 0 and raw[0] in "ABCD" and "ABCD".index(raw[0]) == q["answer"]
        print(ui["correct"] if ok else f"{ui['wrong']} {'ABCD'[q['answer']]}. {q['options'][q['answer']]}")
        st.record(q, ok)
    show_report(st, lang, ui)
    if st.done():
        print(ui["done"])
    return st

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--lang", choices=["en", "te"], default="en")
    ap.add_argument("--demo", action="store_true", help="simulated learner (synthetic data)")
    a = ap.parse_args()
    if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
        sys.stdout.reconfigure(encoding="utf-8")
    run(a.lang, a.demo)
