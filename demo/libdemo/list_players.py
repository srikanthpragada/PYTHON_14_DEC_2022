from datetime import *

f = open("players.txt", "rt")
for line in f.readlines():
    try:
        name, dob_str = line.strip().split(",")
        dob = datetime.strptime(dob_str, '%d-%m-%Y')
        years = (datetime.now() - dob).days // 365
        print(f"{name:20} {years:3}")
    except:
        pass

f.close()
