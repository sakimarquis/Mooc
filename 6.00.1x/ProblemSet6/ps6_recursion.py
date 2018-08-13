# 6.00x Problem Set 6
#
# Part 2 - RECURSION

#
# Problem 3: Recursive String Reversal
#
def reverseString(aStr):
    """
    Given a string, recursively returns a reversed copy of the string.
    For example, if the string is 'abc', the function returns 'cba'.
    The only string operations you are allowed to use are indexing,
    slicing, and concatenation.
    
    aStr: a string
    returns: a reversed string
    """
    if len(aStr) == 1:
        return aStr
    return reverseString(aStr[-1])+reverseString(aStr[0:-1])


#
# Problem 4: X-ian
#
def x_ian(x, word):
    """
    Given a string x, returns True if all the letters in x are
    contained in word in the same order as they appear in x.

    >>> x_ian('eric', 'meritocracy')
    True
    >>> x_ian('eric', 'cerium')
    False
    >>> x_ian('john', 'mahjong')
    False
    x: a string
    word: a string
    returns: True if word is x_ian, False otherwise
    """
    for i in x:
        if i not in word:
            return False
        word = word[word.find(i):]
    return True

def x_ianRecur(x, word):
    if len(x) == 1:
        if x in word:
            return True
        return False
    return x_ianrecur(x[1:],word[word.find(x[1]):])


#
# Problem 5: Typewriter
#
def insertNewlines(text, lineLength):
    """
    Given text and a desired line length, wrap the text as a typewriter would.
    Insert a newline character ("\n") after each word that reaches or exceeds
    the desired line length.

    text: a string containing the text to wrap.
    line_length: the number of characters to include on a line before wrapping
        the next word.
    returns: a string, with newline characters inserted appropriately. 
    """
    list = []
    output = ''
    for i in range(len(text)/lineLength):
        list.append(text[:lineLength])
        text = text[lineLength:]
    list.append(text)
    for j in list:
        output = output + j + "\n"
    return output

def insertNewlinesRecur(text, lineLength):
    output = ''
    if len(text) <= lineLength:
        return output + text
    return insertNewlinesRecur(text[:lineLength], lineLength) + "\n" + insertNewlinesRecur(text[lineLength:], lineLength)


print insertNewlinesRecur('sdfasdffafwefawefwefaweafwfwefp', 3)

