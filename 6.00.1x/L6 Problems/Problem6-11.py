def biggest(aDict):
    num = 0
    for i in aDict:
        num = max(num, len(aDict[i]))
    for j in aDict:
        if len(aDict[j]) == num:
            return j

def biggest1(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    result = None
    biggestValue = 0
    for key in aDict.keys():
        if len(aDict[key]) >= biggestValue:
            result = key
            biggestValue = len(aDict[key])
    return result