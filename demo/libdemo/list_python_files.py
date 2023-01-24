import os

entries = os.walk(r"d:\classroom\nov14p\demo")

count = 0
for (dirname, folders, files) in entries:
   for file in files:
       if file.endswith(".py"):
           print(dirname + "\\" + file)
           count += 1


print("Count = ", count)


