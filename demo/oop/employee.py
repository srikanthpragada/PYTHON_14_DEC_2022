class Employee:
    # Class attribute or Static attribute
    hraper = 35

    @staticmethod
    def gethraper():
        return Employee.hraper

    # constructor
    def __init__(self, name, salary=0):
        # Object Attributes
        self.name = name
        self.salary = salary

    # Methods
    def net_salary(self):
        hra = self.salary * Employee.hraper / 100
        return self.salary + hra

    def get_hra(self):
        return self.salary * Employee.hraper / 100

    def change_salary(self, newsalary):
        if newsalary > self.salary:
            self.salary = newsalary


print(Employee.gethraper())

e1 = Employee("Steve", 60000)  # calls constructor __init__()
print(e1.name)
e1.change_salary(75000)
print(e1.net_salary())

e2 = Employee("Bill")
