def laceStrings(s1, s2):
    ans = ''
    for a in range(min(len(s1),len(s2))):
        ans = ans + s1[a] + s2[a]
    for b in s1[min(len(s1),len(s2)):]:
        ans = ans + b
    for c in s2[min(len(s1),len(s2)):]:
        ans = ans + c
    return ans

print laceStrings('abcd', 'efghi')
