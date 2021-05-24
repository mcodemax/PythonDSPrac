def two_list_dictionary(keys, values):
    """Given keys and values, make dictionary of those.
    
        >>> two_list_dictionary(['x', 'y', 'z'], [9, 8, 7])
        {'x': 9, 'y': 8, 'z': 7}
        
    If there are fewer values than keys, remaining keys should have value
    of None:
    
        >>> two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3])
        {'a': 1, 'b': 2, 'c': 3, 'd': None}
    
    If there are fewer keys, ignore remaining values:

        >>> two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4])
        {'a': 1, 'b': 2, 'c': 3}
   """
    ind = 0
    ret_dict = {}
    bigger_list_len = 0
    smaller_list_len = 0
    if len(keys) > len(values):

        for i in range(len(keys)):
            if i > len(values) - 1:
                ret_dict[keys[i]] = None
            else:
                ret_dict[keys[i]] = values[i]
            
    else:
        for i in range(len(keys)):
            ret_dict[keys[i]] = values[i]
    
    return ret_dict
    # while ind < bigger_list_len:
    #     if bigger_list_len > smaller_list_len
    #     ret_dict[keys[ind]] = values[ind]
    #     ind+=1