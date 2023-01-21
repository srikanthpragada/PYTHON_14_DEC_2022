# take names from user and write them into file - names.txt

f = open("names.txt", "at")

while True:
    name = input("Enter name [end to stop] :")
    if name == "end":
        break

    f.write(name + "\n")

f.close()
