def myLog(x,b):
    power = 0
    while b ** power <= x:
        power += 1
    return power - 1


print  myLog(4,16)