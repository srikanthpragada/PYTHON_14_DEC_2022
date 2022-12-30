first = ['Jack', 'Keven', 'Larry', 'Scott']
last = ['Dorsey', 'Logins', "Page"]

for idx, name in enumerate(first):
    if idx < len(last):
        print(name, last[idx])
    else:
        print(name)
