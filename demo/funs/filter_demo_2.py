names = ["C", "C++", "Java", "Python", "C#"]


def largename(s) -> bool:
    return len(s) < 3


for n in filter(largename, names):
    print(n)
