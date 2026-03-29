from word_count import count, reading_time, flesch_kincaid, word_freq
stats = count("Hello world. This is a test.")
assert stats["words"] == 6
assert stats["sentences"] == 2
assert reading_time(238) == "1 min"
assert reading_time(500) == "3 min"
freq = word_freq("the cat sat on the mat the")
assert freq[0] == ("the", 3)
print("Word count tests passed")