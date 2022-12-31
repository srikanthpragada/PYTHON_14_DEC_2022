data = [(1, 50), (3, 60), (1, 80), (2, 80), (2, 50), (2, 90)]

students = {}
for rollno, marks in data:
    if rollno in students:
        students[rollno] = students[rollno] + marks
    else:
        students[rollno] = marks

print(students)
