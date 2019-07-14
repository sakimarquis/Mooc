# implementation of card game - Memory
import simplegui
import random

# helper function to initialize globals
def new_game():
    global state, first, second, turn, decks, exposed, exposed_init
    state,first,second,turn = 0, 0, 0, 0
    decks = [x for x in range(8)] * 2
    random.shuffle(decks)
    exposed = [False] * 16
    label.set_text('Turns = %d' % turn)
    
# define event handlers
def mouseclick(pos):
    global state, exposed, first, second, turn
    if exposed[pos[0] // 50] == 0:
        if state != 1:
            if state == 2 and decks[first] != decks[second]:
                exposed[first] = 0
                exposed[second] = 0
            first = pos[0] // 50
            exposed[first] = 1
            state = 1            
        elif state == 1:
            second = pos[0] // 50
            exposed[second] = 1
            state = 2
            turn += 1
            label.set_text('Turns = %d' % turn)
        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for i in range(len(decks)):
        start = 50 * i
        canvas.draw_text(str(decks[i]), (start+6, 75), 60, 'White')
        if not exposed[i]:
            rectangle = [[start, 0], [start, 100], [start + 50, 100], [start + 50, 0]]
            canvas.draw_polygon(rectangle, 3, 'Yellow', 'Orange')

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
