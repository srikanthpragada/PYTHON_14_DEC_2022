class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # called when object is converted to str
    def __str__(self):
        return self.name + " - " + str(self.age)

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __gt__(self, other):
        return self.age > other.age

    def __int__(self):
        return self.age


p1 = Person("A", 30)
p2 = Person("B", 25)
p3 = Person("B", 25)

print(p1)  # str(p1)
print(str(p1))  # p1.__str__()
print(p2 == p3)  # p2.__eq__(p3)
print(p1 > p2)  # p1.__gt__(p2)

people = [p1, p2, p3]
for p in sorted(people):
    print(p)