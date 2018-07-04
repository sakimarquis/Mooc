import simplegui
import random

num_range = 100

def new_game():
    global secret_number,num_range,count
    secret_number = random.randrange(0, num_range)
    count = 7
    if num_range == 1000: 
        count = 10
    print "New game. range is from 0 to %i." % num_range

def range100():
    global num_range
    num_range = 100
    return new_game()

def range1000():
    global num_range
    num_range = 1000
    return new_game()
    
def get_input(guess): 
    try:
        print "Guess was %i." % int(guess)
    except:
        print "Bad input. Restarting.....\n"
        return new_game()
    
    global count
    count -= 1
    print "Number of remaining guesses is %i." % count
    
    if int(guess) == secret_number:
        print "Correct!  :)\n"
        return new_game()
    if count > 0: 
        if int(guess) > secret_number:
            print "Lower!\n"
        else:
            print "Higher!\n"
    else:
        print "You ran out of guesses. The number was %i.  :(\n" % secret_number
        return new_game()


f = simplegui.create_frame("Guess the number", 200, 200)
f.add_button("Range is [0, 100)", range100, 200)
f.add_button("Range is [0, 1000)", range1000, 200)
f.add_input("Enter a guess", get_input, 200)

new_game()
