total = 0
for i in range(5):
    s = input("Enter number :")
    try:
        total += int(s)
    except ValueError:
        print("Sorry! Invalid Number!")


print("Total = ", total)
