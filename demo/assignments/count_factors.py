# Print count of factors

num = int(input("Enter number :"))
count = 0
for i in range(2, num // 2 + 1):
    if num % i == 0:
        count += 1  # count = count + 1

print("Count = ", count)
