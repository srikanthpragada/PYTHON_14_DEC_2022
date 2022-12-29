s = "how do you do"

chars = []
for c in s:
    if c not in chars:
        print(f"{c} - {s.count(c)}")
        chars.append(c)

