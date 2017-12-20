def oddTuples(aTup):
    """
    aTup: a tuple

    returns: tuple, every other element of aTup.
    """
    # slicing by 2
    return aTup[::2]

    # or it can be solved
    # rTup = ()
    # index = 0
    # while index < len(aTup):
    #     rTup += (aTup[index],)    # here's using (aTup[index],) and not aTup[index] because I need the tuple itself not the primitive data inside it.

    #     index += 2
    # return rTup


print(oddTuples((5, 2, 7, 4, 1, 16)))
