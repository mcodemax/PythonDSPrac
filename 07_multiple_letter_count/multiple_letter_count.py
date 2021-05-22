def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """

    ltr_dict = {}

    for letter in phrase:
        if letter in ltr_dict: #has_key() method no longer supported in python3
            ltr_dict[letter]+=1
        else:
            ltr_dict[letter] = 1 
            

    return ltr_dict