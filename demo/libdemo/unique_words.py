import re

with open("test.txt", "rt") as f:
    contents = f.read()

words = set(re.findall(r'\w+', contents))
print(sorted(words))
