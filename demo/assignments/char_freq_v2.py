s = "how do you do"

chars = {}
for c in set(s):
    chars[c] = s.count(c)


for k, v in sorted(chars.items()):
    print(k, v)

