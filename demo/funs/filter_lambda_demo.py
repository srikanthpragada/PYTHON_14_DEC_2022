nums = [10, 21, 34, 44, 55, 32, 11]

for n in filter(lambda v : v % 2 == 0, nums):
    print(n)
