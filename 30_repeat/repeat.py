def repeat(phrase, num):
    """Return phrase, repeated num times.

        >>> repeat('*', 3)
        '***'

        >>> repeat('abc', 2)
        'abcabc'

        >>> repeat('abc', 0)
        ''

    Ignore illegal values of num and return None:

        >>> repeat('abc', -1) is None
        True

        >>> repeat('abc', 'nope') is None
        True
    """
    count = 0
    ret_phrase = ''

    if isinstance(num, int) == 0:
        return
    if num >= 0:
        if num == 0:
            return ret_phrase
        
        for i in range(num):    
            ret_phrase+=phrase
        return ret_phrase

   
