# read marks and display total

f = open("marks.txt", "rt")

total = 0
for line in f.readlines():
     total += int(line.strip())

f.close()
print("Total = ", total)
