"""
simulation for Monte Hall problem
"""

import random

MIN_DOORS = 3
MAX_DOORS = 10

class MontyHall:
    def __init__(self):
        """
        Initialize the simulation
        """
        self._wins = 0
        self._loses = 0
        self._num_doors = MIN_DOORS
        self._prize_door = random.randrange(self._num_doors)

    def start(self, door_num, change):
        """
        Process a valid door number based on state
        """
        self._selected_door = door_num
        self.show()
        if change:
            self.change()
        self.is_win()
        
    def show(self):
        if self._selected_door == self._prize_door:
            doors = range(self._num_doors)
            doors.remove(self._selected_door)
            doors.remove(random.choice(doors))
            self._remain = doors[0]
        else:
            self._remain = self._prize_door        
    
    def change(self):
        """
        change selected door or not
        """
        self._selected_door = self._remain   
            
    def is_win(self):
        """
        Determine if win
        """
        if self._selected_door == self._prize_door:
            self._wins += 1
        else:
            self._loses += 1
        self._prize_door = random.randrange(self._num_doors)
    
    def change_door_num(self, num):
        """
        change the number of the doors in the simulation
        """
        self._num_doors = num
        
    def state(self):
        return "Selected is No.%d, Remain is No.%d, Prized is %d." % (self._selected_door, self._remain, self._prize_door)

    def __str__(self):
        return "Win %d times, lose %d times" % (self._wins, self._loses)

game = MontyHall()
for i in range(1000):
    game.start(0, True)
    print game.state()

print game.__str__()
        
