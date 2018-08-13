class Point:
  pass

blank = Point()
blank.x = 3.0
blank.y = 4.0

print blank.y
x = blank.x
print x

print '(' + str(blank.x) + ', ' + str(blank.y) + ')'
distanceSquared = blank.x * blank.x + blank.y * blank.y
print distanceSquared

print blank

def printPoint(p):
  print '(' + str(p.x) + ', ' + str(p.y) + ')'

print printPoint(blank)



p1 = Point()
p1.x = 3
p1.y = 4
p2 = Point()
p2.x = 3
p2.y = 4

p1 is p2