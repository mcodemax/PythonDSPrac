def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which are not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
                       'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """

    backwards_s_vowel_storage = ''

    #stores vowels read backwards into a string
    for char in s[::-1]:
        if char in 'aeiouAEIOU':
            backwards_s_vowel_storage+=char
    
    print(backwards_s_vowel_storage)
    #for char in s
    
    ret_str = ''
    backwards_s_vowel_storage_ind = 0
    for char in s:
        if char in 'aeiouAEIOU':
            ret_str+=backwards_s_vowel_storage[backwards_s_vowel_storage_ind]
            backwards_s_vowel_storage_ind+=1
        else:
            ret_str+=char

    return ret_str
    