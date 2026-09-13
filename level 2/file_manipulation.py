from collections import Counter
import re

with open("sample.txt", "r", encoding="utf-8") as file:
    text = file.read()

words = re.findall(r"[A-Za-z0-9]+", text.lower())

word_count = Counter(words)

print("Word counts:")

for word in sorted(word_count):
    print(word, ":", word_count[word])
    