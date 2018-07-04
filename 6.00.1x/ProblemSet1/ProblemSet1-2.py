#2,COUNTING BOBS
s= 'azcbobobeggbobbobobhakl'
def CountBob(s):
    result = 0
    x = s.find('bob')
    while x != -1:
        result +=1
        x = s.find('bob',x+2)
    return result

print 'Number of times bob occurs is: ' + str(CountBob(s))