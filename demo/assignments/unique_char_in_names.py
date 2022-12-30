names = ['java', 'c', 'python', 'javascript', 'ruby']

chars = set()
for n in names:
    chars = chars | set(n)

print(chars)


