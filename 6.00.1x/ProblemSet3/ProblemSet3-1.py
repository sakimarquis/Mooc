def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)

def radiationExposure(start, stop, step):
    result = 0
    while stop > start:
        result += step*f(start)
        start += step
    return result

def radiationExposureRecur(start, stop, step):
    if stop <= start:
        return 0
    else:
        return step*f(start) + radiationExposureRecur(start+step, stop, step)

print radiationExposure(0,5,1)
print radiationExposureRecur(0,5,1)