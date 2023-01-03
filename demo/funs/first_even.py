def first_even(*nums):
    for n in nums:
        if n % 2 == 0:
            return n

    return None  # No even number found so return None


print(first_even(11, 35, 40, 50), first_even(11, 33, 89))
