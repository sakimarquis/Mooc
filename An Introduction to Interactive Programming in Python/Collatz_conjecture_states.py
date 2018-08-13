import simplegui

max = 0

def init(start):
    global n,result
    n = float(start)
    print "Input is", n

def get_next(current):
    global max
    if current > max:
        max = current
    if current % 2 == 0:
        return current/2
    else:
        return current*3 + 1

def update():
    global n
    if n == 1:
        timer.stop()
        print "Output is", max
    else:
        n = get_next(n)

timer = simplegui.create_timer(1, update)

init(23)
timer.start()
