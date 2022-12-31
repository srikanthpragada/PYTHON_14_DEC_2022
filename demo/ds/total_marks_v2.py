data = [(1, 50), (3, 60), (1, 80), (2, 80), (2, 50), (2, 90)]

students = {}
for rollno, marks in data:
     total = students.get(rollno, 0)
     students[rollno] = total + marks

print(students)
