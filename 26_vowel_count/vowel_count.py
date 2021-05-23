def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """

    vowels = ['a','e','i','o','u']
    phrase_dict = {}
        
    for letter in phrase:
        if letter in vowels:
            if letter in phrase_dict:
                phrase_dict[letter]+=1
            else:
                phrase_dict[letter] = 1

    return phrase_dict
