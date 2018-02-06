def uniqueValues(aDict):
    """
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    """
    try:
        ls = list(aDict.values())
    except AttributeError:
        return []
    returnedList = []
    setLs = list(set(ls))
    for item in ls:
        try:
            if ls.count(item) > 1:
                setLs.remove(item)
        except ValueError:
            continue
    list(setLs)
    for item in setLs:
        returnedList.append(list(aDict.keys())[list(aDict.values()).index(item)])
    return returnedList


# print(uniqueValues({1: 1, 3: 2, 6: 0, 7: 0, 8: 4, 10: 0}))
# print(uniqueValues({1: 1, 2: 1, 3: 1}))
# print(uniqueValues({1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 7: 0, 8: 0, 9: 15}))
# print(uniqueValues({0}))
