# read names from names.txt and print them

f = open("names.txt", "rt")
for line in f.readlines():
    print(line.strip())

f.close()
