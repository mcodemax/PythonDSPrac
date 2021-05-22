def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    num_dict = {}

    most_common_id = None
    most_common_count = 0
    for i in nums:
        if i in num_dict.keys():
            num_dict[i]+=1
        else:
            num_dict[i] = 1

    for (k, v) in num_dict.items():
        if v > most_common_count:
            most_common_count = v
            most_common_id = k

    if most_common_count == 0:
        return
    else:
        return most_common_id

