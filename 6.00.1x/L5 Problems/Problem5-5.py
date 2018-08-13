def gcdRecur(a, b):
    if min(a,b) == 0 :
        return max(a,b)
    return  gcdRecur(min(a,b),max(a,b)%min(a,b))

def gcdRecur1(a, b):
    if b == 0:
        return a
    return gcdRecur1(b, a % b)

print gcdRecur1(165, 120)