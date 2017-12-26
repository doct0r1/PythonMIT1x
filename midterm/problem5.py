def uniqueValues(aDict):
    """
    aDict: a dictionary
    """
    countMap = {}
    for v in aDict.values():
        countMap[v] = countMap.get(v,0) + 1
    uni = [ k for k, v in aDict.items() if countMap[v] == 1] 
    return uni
