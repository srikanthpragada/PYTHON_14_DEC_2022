first = ['Jack', 'Keven', 'Larry', 'Scott', 'Jason']
last = ['Dorsey', 'Logins', "Page"]

diff = len(first) - len(last)
last.extend([''] * diff)

for fname, lname in zip(first, last):
    print(fname, lname)
