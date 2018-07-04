class Weird(object):
    def __init__(self, x, y): 
        self.y = y
        self.x = x
    def getX(self):
        return x 
    def getY(self):
        return y

class Wild(object):
    def __init__(self, x, y): 
        self.y = y
        self.x = x
    def getX(self):
        return self.x 
    def getY(self):
        return self.y

X = 7
Y = 8

w2 = Wild(X, Y)
w3 = Wild(17, 18)
w4 = Wild(X, 18)
X = w4.getX() + w3.getX() + w2.getX()
print X
print w4.getX()

Y = w4.getY() + w3.getY()
Y = Y + w2.getY()
print Y
print w2.getY()