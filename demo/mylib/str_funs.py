def count_upper(s):
    count = 0
    for c in s:
        if c.isupper():
            count += 1

    return count


def has_digit(s):
    for c in s:
        if c.isdigit():
            return True

    return False


# Execute code when module is run as script
if __name__ == '__main__':
    print(has_digit('Abc'))
