# Varying args
def wish(*names, message='Hello'):
    for n in names:
        print(message, n)


wish("Scott", "Tom")
wish("Larry", "Joe", "Andy", message="Hi")
