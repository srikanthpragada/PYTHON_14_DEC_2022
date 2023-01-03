def process(task, p1, p2):
    print(task(p1, p2))


def add(n1, n2):
    return n1 + n2


process(add, 10, 20)  # passing a fun as parameter
