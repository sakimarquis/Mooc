def lenRecur(aStr):
    if aStr =='':
        return 0
    return lenRecur(aStr[1:]) + 1

print  lenRecur('sfd424f')
