# read data from employees.txt and display dept and employees

f = open("employees.txt", "rt")
depts = {}

for line in f.readlines():
    parts = line.split(",")
    if len(parts) < 2:
        continue      # ignore line

    dname = parts[0].strip()
    ename = parts[1].strip()

    if dname in depts:
        depts[dname].append(ename)   # add name to list
    else:
        depts[dname] = [ename]

f.close()

for dname, employees in depts.items():
    print(dname, ",".join(employees))


