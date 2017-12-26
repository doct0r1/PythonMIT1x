def gcd(a, b):
    """
    a, b: two positive integers
    Returns the greatest common divisor of a and b
    """
    while b:
        # print('b: ', b)
        # print('a: ', a)
        a, b = b, a%b
    return a

# print(gcd(15, 5))
# print('done')
# print(gcd(112, 12))
