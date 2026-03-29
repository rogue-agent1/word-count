#!/usr/bin/env python3
"""Word/character/line counter with readability metrics. Zero dependencies."""
import re, sys, math

def count(text):
    lines = text.splitlines()
    words = text.split()
    chars = len(text)
    chars_no_space = len(text.replace(" ", "").replace("\n", "").replace("\t", ""))
    sentences = len(re.findall(r"[.!?]+", text))
    paragraphs = len([p for p in re.split(r"\n\s*\n", text) if p.strip()])
    return {
        "lines": len(lines), "words": len(words), "chars": chars,
        "chars_no_space": chars_no_space, "sentences": max(sentences, 1),
        "paragraphs": max(paragraphs, 1),
    }

def reading_time(word_count, wpm=238):
    minutes = word_count / wpm
    if minutes < 1: return "< 1 min"
    return f"{math.ceil(minutes)} min"

def flesch_kincaid(text):
    stats = count(text)
    words = text.split()
    if not words: return 0
    syllables = sum(_count_syllables(w) for w in words)
    score = 206.835 - 1.015 * (stats["words"]/stats["sentences"]) - 84.6 * (syllables/stats["words"])
    return round(score, 1)

def _count_syllables(word):
    word = word.lower().strip(".,!?;:'\"-")
    if not word: return 0
    count = 0; prev_vowel = False
    for c in word:
        is_vowel = c in "aeiouy"
        if is_vowel and not prev_vowel: count += 1
        prev_vowel = is_vowel
    if word.endswith("e") and count > 1: count -= 1
    return max(count, 1)

def word_freq(text, top=10):
    words = re.findall(r"\b[a-zA-Z]+\b", text.lower())
    freq = {}
    for w in words: freq[w] = freq.get(w, 0) + 1
    return sorted(freq.items(), key=lambda x: -x[1])[:top]

if __name__ == "__main__":
    text = sys.stdin.read() if len(sys.argv) < 2 else open(sys.argv[1]).read()
    stats = count(text)
    for k, v in stats.items():
        print(f"{k:>15}: {v}")
    print(f"{'reading_time':>15}: {reading_time(stats['words'])}")
    print(f"{'flesch_kincaid':>15}: {flesch_kincaid(text)}")
