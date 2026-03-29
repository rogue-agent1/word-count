#!/usr/bin/env python3
"""Word frequency counter."""
import re

STOP_WORDS = frozenset("a an the and or but in on at to for of is it this that was were be been being "
    "have has had do does did will would shall should may might can could with from by as are am".split())

def count_words(text: str, stop_words: bool = True) -> dict:
    words = re.findall(r'\b[a-z]+\b', text.lower())
    if stop_words:
        words = [w for w in words if w not in STOP_WORDS]
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    return freq

def top_words(text: str, n: int = 10, stop_words: bool = True) -> list:
    freq = count_words(text, stop_words)
    return sorted(freq.items(), key=lambda x: -x[1])[:n]

def word_stats(text: str) -> dict:
    words = text.split()
    if not words:
        return {"total": 0, "unique": 0, "avg_length": 0}
    unique = set(w.lower().strip(".,!?;:") for w in words)
    avg_len = sum(len(w) for w in words) / len(words)
    return {"total": len(words), "unique": len(unique), "avg_length": round(avg_len, 2)}

if __name__ == "__main__":
    import sys
    text = " ".join(sys.argv[1:]) or "the quick brown fox jumps over the lazy dog"
    for word, count in top_words(text):
        print(f"  {count:4d}  {word}")

def test():
    text = "the cat sat on the mat the cat"
    freq = count_words(text, stop_words=True)
    assert freq["cat"] == 2
    assert freq["sat"] == 1
    assert freq["mat"] == 1
    assert "the" not in freq
    # Without stop words
    freq2 = count_words(text, stop_words=False)
    assert freq2["the"] == 3
    # Top words
    top = top_words(text)
    assert top[0][0] == "cat"
    # Stats
    stats = word_stats("hello world hello")
    assert stats["total"] == 3
    assert stats["unique"] == 2
    # Empty
    assert word_stats("")["total"] == 0
    print("  word_count: ALL TESTS PASSED")
