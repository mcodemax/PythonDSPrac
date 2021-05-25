def three_odd_numbers(nums):
    """Is the sum of any 3 sequential numbers odd?"

        >>> three_odd_numbers([1, 2, 3, 4, 5])
        True

        >>> three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0])
        True

        >>> three_odd_numbers([5, 2, 1])
        False

        >>> three_odd_numbers([1, 2, 3, 3, 2])
        False
    """
    
    ind = 0
    while ind < len(nums) - 2:
        #print(nums[ind], nums[ind+1], nums[ind+2])
        if (nums[ind] + nums[ind+1] + nums[ind+2]) % 2 == 1:
            return True
        ind+=1
    return False