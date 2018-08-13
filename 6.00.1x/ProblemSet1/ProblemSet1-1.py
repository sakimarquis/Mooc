#1,COUNTING VOWELS
#s= 'adsfafsiodf'
def CountVowel(s):
    result =  0
    for i in ('a', 'e', 'i', 'o', 'u'):
        result += s.count(i)
    return result
print 'Number of vowels: ' + str(CountVowel(s))





