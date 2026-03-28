#!/usr/bin/env python3
"""word_count - Count words, lines, chars, and more."""
import sys, os, re, json
def count(text):
    lines = text.count("\n"); words = len(text.split()); chars = len(text)
    sents = len(re.findall(r"[.!?]+", text)); paras = len(re.split(r"\n\n+", text.strip()))
    avg_word = sum(len(w) for w in text.split()) / max(words,1)
    return {"lines":lines,"words":words,"chars":chars,"sentences":sents,"paragraphs":paras,"avg_word_len":round(avg_word,1)}
if __name__ == "__main__":
    if len(sys.argv) > 1:
        for f in sys.argv[1:]:
            c = count(open(f).read()); print(f"{c['lines']:>7} {c['words']:>7} {c['chars']:>7} {f}")
    else:
        c = count(sys.stdin.read())
        for k,v in c.items(): print(f"{k}: {v}")
