def is_increasing(digits: list) -> bool:
    '''
    The idea for this function will be to compare index by index
    to see if i > i+1.
    '''

    if len(digits) == 0:
        return True

    for i in range(0,len(digits)-1):

        if digits[i] < digits[i+1]:
            continue
        else:
            return False
    return True
