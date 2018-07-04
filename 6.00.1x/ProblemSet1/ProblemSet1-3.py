# -*- coding: utf-8 -*-
#3,ALPHABETICAL SUBSTRINGS
s= 'rqwazqhhkwfkknlklj'
def ABC(s):
    result = s[0]
    longest = result
    for i in range(len(s)-1):
        if s[i]<=s[i+1]:
            result += (s[i+1])
            if len(result) > len(longest):
                longest = result
        else:
            result = s[i+1]
    return longest

print ABC(s)

