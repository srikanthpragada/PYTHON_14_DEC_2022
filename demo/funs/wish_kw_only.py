# Keyword-only args
def wish(*,  user='Guest', message="Hi"):
    print(message, user)


wish(user="Joe", message="Good Morning")
wish(user="Mark")
wish()
