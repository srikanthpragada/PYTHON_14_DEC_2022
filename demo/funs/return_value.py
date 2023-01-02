def count_upper(s: str) -> int:
    count = 0
    for c in s:
        if c.isupper():
            count += 1

    return count


def iseven(n: int) -> bool:
    return n % 2 == 0


c = count_upper("AbCD")
#c = count_upper(3939393)
print(c)
