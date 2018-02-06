def is_triangular(k):
    """
    :param k: a positive integer
    :return: True if k is triangular and False if not
    """
    for i in range(k):
        if i * (i + 1) / 2 == k:
            return True
    return False
