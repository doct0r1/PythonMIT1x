animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati'], 'd': ['donkey']}

animals['d'].append('dog')
animals['d'].append('dingo')

def how_many(aDict):
    """
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    """

    # since all values in dict are lists, dict.values() will be a list of lists
    counter = 0
    for val in aDict.values():
       counter += len(val)
    return counter

    # or
    # it can be solved by keys
    # as every values in dictionary will be assigned w/ a key for instance if the values is a list of 2 values then the key can point to both values

    # counter1 = 0
    # for key in aDict.keys():
    #     counter1 += len(aDict[key])
    #

print(how_many(animals))
