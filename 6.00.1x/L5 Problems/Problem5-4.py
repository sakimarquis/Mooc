def gcdIter(a,b):
    i = min(a,b)
    while a % i != 0 or b % i !=0:
        i -= 1
    return i
