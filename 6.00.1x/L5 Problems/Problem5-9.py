def semordnilap(str1, str2):
    a = 0
    b = -1
    if len(str1) ==1 or len(str2) == 1:
        return False
    if len(str1) != len(str2):
        return False
    if str1[0]==str2[-1]:
        return True
    return semordnilap(str1[a+1], str2[b-1])

print semordnilap('vaabcd', 'dcbaav')