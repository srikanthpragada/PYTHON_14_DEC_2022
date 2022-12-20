# Take marks until -1 is given and display total
total = 0
while True:
    marks = int(input("Enter marks [-1 to stop]:"))
    if marks == -1:
        break
    total = total + marks

print("Total = ", total)
