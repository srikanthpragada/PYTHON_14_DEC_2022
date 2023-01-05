data = ["ab123", "12X34", "E889"]


def extract_digits(s):
    ns = ""
    for c in s:
        if c.isdigit():
            ns = ns + c

    return ns


for s in map(extract_digits, data):
    print(s)
