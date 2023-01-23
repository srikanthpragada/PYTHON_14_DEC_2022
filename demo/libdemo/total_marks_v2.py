# read marks and display total

with open("marks.txt", "rt") as f:
    total = sum(map(int, f.readlines()))

print("Total = ", total)
