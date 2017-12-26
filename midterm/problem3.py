def jumpAndBackpedal(isMyNumber):
    """
    isMyNumber: Procedure that hides a secret number.
     It takes as a parameter one number and returns:
     *  -1 if the number is less than the secret number
     *  0 if the number is equal to the secret number
     *  1 if the number is greater than the secret number

    returns: integer, the secret number
    """
    """
    Note:
    This problem not working for me!!!!! 
    """

    guess = 1
    if isMyNumber == guess:
        return guess - 1
    foundNumber = False
    while not foundNumber:
        sign = isMyNumber
        if sign < 1:
            guess = -1
        else:
            guess = 1
    return guess

print(jumpAndBackpedal(0))

