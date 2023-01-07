def count_upper(s):
    """
    Counts number of uppercase letters in the given string
    :param s: Input string
    :return: Count of uppercase letters
    """
    count = 0
    for c in s:
        if c.isupper():
            count += 1

    return count


def has_digit(s):
    """
    Checks whether a string has any digit
    :param s: Input string
    :return:  True if string has any digit otherwise false
    """
    for c in s:
        if c.isdigit():
            return True

    return False


# Execute code when module is run as script
if __name__ == '__main__':
    print(has_digit('Abc'))
