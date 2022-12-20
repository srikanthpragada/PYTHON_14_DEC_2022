# Take either 5 marks or until -1 is given
total = 0
for i in range(5):
    marks = int(input("Enter marks [-1 to stop]:"))
    if marks == -1:
        break
    total = total + marks

print("Total = ", total)
