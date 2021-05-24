def min_max_keys(d):
    """Return tuple (min-keys, max-keys) in d.

        >>> min_max_keys({2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'})
        (1, 10)

    Works with any kind of key that can be compared, like strings:

        >>> min_max_keys({"apple": "red", "cherry": "red", "berry": "blue"})
        ('apple', 'cherry')
    """

    min_key = None
    max_key = None
    for i in d.keys():
        if min_key == None or i < min_key:
            min_key = i
        if max_key == None or i > max_key or min_key == None:
            max_key = i

    return (min_key, max_key)

