def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """

    num_dict_1 = {}

    for i in str(num1):
        if i in num_dict_1.keys():
            num_dict_1[i]+=1
        else:
            num_dict_1[i] = 1
    
    for i in str(num2):
        if i in num_dict_1.keys():
            num_dict_1[i]-=1
        else:
            return False

    for val in num_dict_1.values():
        if val != 0:
            return False
    
    return True
        
