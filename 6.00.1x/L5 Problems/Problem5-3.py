def recurPowerNew(base, exp):
    if exp == 0:
        return  1
    if exp > 0 and exp % 2 == 0:
        return recurPowerNew(base, exp/2) * recurPowerNew(base, exp/2)
    else:
        return base * recurPowerNew(base, exp - 1)