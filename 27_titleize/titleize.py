def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    #if previous index has space caps it

    string = ''

    # for ltr in phrase:
    #     if or phrase[]

    i = 0
    while i < len(phrase):
        if i == 0:
            string+=phrase[i].upper()
        elif i > 0 and phrase[i - 1] == ' ':
            string+=phrase[i].upper()
        else:
            string+=phrase[i].lower()
        
        i+=1
    return string