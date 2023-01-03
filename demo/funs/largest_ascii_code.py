def largest_code(*values):
    lcode = 0
    for v in values:
        for c in v:
            if ord(c) > lcode:
                lcode = ord(c)

    return lcode


print(largest_code('abc', 'DEF', 'XYZ', 'Pqr'))
