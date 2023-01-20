total = 0
i = 1
while i <= 5:
    s = input("Enter number :")
    try:
        total += int(s)
        i = i + 1
    except ValueError:
        print("Sorry! Invalid Number!")


print("Total = ", total)
