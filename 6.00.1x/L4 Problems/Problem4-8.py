def fourthPower(x):
    def square(x):
        x = x * x
        return x
    return square(square(x))