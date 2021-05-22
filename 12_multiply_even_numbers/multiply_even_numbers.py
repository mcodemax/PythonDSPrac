def multiply_even_numbers(nums):
    """Multiply the even numbers.
    
        >>> multiply_even_numbers([2, 3, 4, 5, 6])
        48
        
        >>> multiply_even_numbers([3, 4, 5])
        4
        
    If there are no even numbers, return 1.
    
        >>> multiply_even_numbers([1, 3, 5])
        1
    """
    product = 1
    even_num_count = 0
    for x in nums:
        if (x % 2) == 0:
            product = product * x
            even_num_count+=1
        
    if(even_num_count > 0):
        return product
    else:
        return 1
