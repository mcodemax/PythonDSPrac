def find_factors(num):
    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """
    lst = []
    biggest_factor = 1
    while(biggest_factor <= num):
        if num % biggest_factor == 0:
            lst.append(biggest_factor)
        biggest_factor+=1
    return lst