# take marks from user and write them into file - names.txt

f = open("marks.txt", "wt")

while True:
    marks = int(input("Enter marks [0 to stop] :"))
    if marks == 0:
        break

    f.write(str(marks) + "\n")

f.close()
