import os

stdir = input("Enter starting directory :")
extension = input("Enter extension : ")

entries = os.walk(stdir)
count = 0
for (dirname, folders, files) in entries:
   for file in files:
       if file.endswith(extension):
           print(dirname + "\\" + file)
           count += 1


print("Count = ", count)


