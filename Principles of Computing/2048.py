"""
Clone of 2048 game.
"""

import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    length = len(line)
    if length == 1:
        return line
    line_copy = list(line) 
    while 0 in line_copy:
        line_copy.remove(0)
    result = []
    if len(line_copy) > 0:
        for number in range(len(line_copy) - 1):
            if line_copy[number] == line_copy[number+1]:
                result.append(line_copy[number]*2)
                line_copy[number+1] = 0
            else:
                result.append(line_copy[number])
        result.append(line_copy[-1])
    while 0 in result:
        result.remove(0)
    while length > len(result):
        result.append(0)   
    return result

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self._height = grid_height
        self._width = grid_width
        self._grid = []
        self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._grid = [[0] * self._width for _ in range(self._height)]
        self.new_tile()
        self.new_tile()
        
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        return str(self._grid)

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        initial = list(self._grid)
        # the first element include the imformation of 
        # how the tiles move in the vertical direction
        # use zip(*arg) to "unzip" (rotate the matrix 
        # through diagonal line)     
        if OFFSETS[direction][0] != 0:
            order = OFFSETS[direction][0]
            tmp = []
            for line in zip(*self._grid):
                tmp.append(merge(list(line)[::order])[::order])
            
            # transform tuple to list then assign to self._grid
            self._grid = []
            for line in zip(*tmp):
                self._grid.append(list(line))
                
        # the second element include the imformation of 
        # how the tiles move in the horizontal direction
        # use [::1] or [::-1] to transform
        elif OFFSETS[direction][1] != 0:
            order = OFFSETS[direction][1]
            for number in range(self._height):
                self._grid[number] = merge(self._grid[number][::order])[::order] 
        if initial != self._grid:
            self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        all_tiles = []
        for number in range(self._height):
            all_tiles += self._grid[number]
        while 0 in all_tiles:
            row = random.randrange(0, self._height)
            col = random.randrange(0, self._width)         
            if self._grid[row][col] == 0:
                if random.randrange(0, 10) == 0:
                    self._grid[row][col] = 4
                else:
                    self._grid[row][col] = 2
                break          
        
    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._grid[row][col]


poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
