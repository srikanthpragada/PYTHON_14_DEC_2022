def add(n1, n2):
    return n1 + n2


add2 = add
print(id(add), id(add2))

print(add(10, 20), add2(10, 20))
