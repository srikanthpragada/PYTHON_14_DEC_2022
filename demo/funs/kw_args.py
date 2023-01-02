def show(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


def details(*args, **kwargs):
    for v in args:
        print(v)
    for k, v in kwargs.items():
        print(k, v)


show(a=10, b=20, c=30)
show(name="Abc", age=20)
details(10, 20, a=100, b="Abc")
