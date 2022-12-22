ls = ''
for i in range(5):
    s = input("Enter string:")
    if len(s) > len(ls):
        ls = s

print("Largest string = ", ls)
