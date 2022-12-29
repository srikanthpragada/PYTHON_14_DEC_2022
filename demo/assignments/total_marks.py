data = "90,33,45,60,87"

total = 0
for m in data.split(","):
    total += int(m)

print(total)