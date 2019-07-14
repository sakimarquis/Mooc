# template for "Stopwatch: The Game"
import simplegui
# define global variables

time = 0
count = 0
success = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(time):
    minutes = time / 600
    seconds = (time - (minutes * 600)) / 10
    dseconds = str(time)[-1]
    return "%d:%02d.%s" % (minutes,seconds,dseconds)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
    
def stop():
    global count,success
    count += 1
    if int(str(time)[-1]) == 0:
        success += 1
    timer.stop()

def reset():
    stop()
    global time,count,success
    time,count,success = 0,0,0

# define event handler for timer with 0.1 sec interval
def stopwatch():
    global time
    time += 1

# define draw handler
def draw(canvas):
    canvas.draw_text(format(time), [50, 110], 36, "White")
    canvas.draw_text(str(success)+'/'+str(count), [150, 25], 28, "Green")
  
# create frame
frame = simplegui.create_frame("Stopwatch: The Game",200,200)

# register event handlers
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, stopwatch)

frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)

# start frame
frame.start()

# Please remember to review the grading rubric
