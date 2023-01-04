nums = [-10, 2, 30, -40, 5]

for n in sorted(nums, key=abs):
    print(n)

names = ["abc", "pq", "defg", "xef", 'defghi']

for n in sorted(names, key=len):
    print(n)
