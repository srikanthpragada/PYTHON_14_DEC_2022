nums = [10, 21, 34, 44, 55, 32, 11]


def iseven(n) -> bool:
    return n % 2 == 0


for n in filter(iseven, nums):
    print(n)
