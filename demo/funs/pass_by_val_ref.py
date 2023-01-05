def zero(n):
    print(id(n))
    n = 0
    print(id(n))


def prepend(lst, v):
    lst.insert(0, v)


a = 100
print(id(a))
zero(a)
print(a)
l = [1, 2]
prepend(l, 10)
print(l)
