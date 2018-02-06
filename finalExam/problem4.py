def primes_list(N):
    """
    N: an integer
    Returns a list of prime numbers
    """
    ls = []
    for num in range(2, N + 1):
        prime = True
        for i in range(2, num):
            if (num % i == 0):
                prime = False
        if prime:
            ls.append(num)
    return ls
