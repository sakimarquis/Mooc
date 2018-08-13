def isVowel2(char):
    for i in ('a','e','i','o','u','A','E','I','O','U'):
        if char == i:
            return True
    if char != i:
        return False

def isVowel3(char):
    if char in 'aeiouAEIOU':
        return True
    else:
        return False

def isVowel4(char):
    return char.lower() in 'aeiou'

print isVowel2('o')