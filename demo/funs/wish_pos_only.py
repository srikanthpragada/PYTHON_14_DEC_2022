# Positional-only args
def wish(user='Guest', message="Hi", /):
    print(message, user)


wish("Good Morning", "Joe")
wish("Mark")
wish()
