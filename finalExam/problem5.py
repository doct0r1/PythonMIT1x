def uniqueValues(aDict):
    """
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    """
    global item
    ls = list(aDict.values())
    setLs = set(ls)
    itemCounter = 0
    for item in ls:
        if item in ls:
            itemCounter += 1
    return list(setLs)