def howMany(aDict):
    result = []
    global elements
    elements = []
    for x in aDict.values():
        result = listelements(x)
    return len(result)
def listelements(x):
    for i in x:
        if type(i) == list or type(i) == tuple:
            listmany(i)
        else:
            elements.append(i)
    return elements



def howMany1(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many individual values are in the dictionary.
    '''
    result = 0
    for value in aDict.values():
        # Since all the values of aDict are lists, aDict.values() will
        #  be a list of lists
        result += len(value)
    return result

def howMany2(aDict):
    '''
    Another way to solve the problem.

    aDict: A dictionary, where all the values are lists.

    returns: int, how many individual values are in the dictionary.
    '''
    result = 0
    for key in aDict.keys():
        result += len(aDict[key])
    return result