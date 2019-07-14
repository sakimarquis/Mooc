"""
Loyd's Fifteen puzzle - solver and visualizer
Note that solved configuration has the blank (zero) tile in upper left
Use the arrows key to swap this tile with its neighbors
"""

import poc_fifteen_gui

class Puzzle:
    """
    Class representation for the Fifteen puzzle
    """

    def __init__(self, puzzle_height, puzzle_width, initial_grid=None):
        """
        Initialize puzzle with default height and width
        Returns a Puzzle object
        """
        self._height = puzzle_height
        self._width = puzzle_width
        self._grid = [[col + puzzle_width * row
                       for col in range(self._width)]
                      for row in range(self._height)]

        if initial_grid != None:
            for row in range(puzzle_height):
                for col in range(puzzle_width):
                    self._grid[row][col] = initial_grid[row][col]

    def __str__(self):
        """
        Generate string representaion for puzzle
        Returns a string
        """
        ans = ""
        for row in range(self._height):
            ans += str(self._grid[row])
            ans += "\n"
        return ans

    #####################################
    # GUI methods

    def get_height(self):
        """
        Getter for puzzle height
        Returns an integer
        """
        return self._height

    def get_width(self):
        """
        Getter for puzzle width
        Returns an integer
        """
        return self._width

    def get_number(self, row, col):
        """
        Getter for the number at tile position pos
        Returns an integer
        """
        return self._grid[row][col]

    def set_number(self, row, col, value):
        """
        Setter for the number at tile position pos
        """
        self._grid[row][col] = value

    def clone(self):
        """
        Make a copy of the puzzle to update during solving
        Returns a Puzzle object
        """
        new_puzzle = Puzzle(self._height, self._width, self._grid)
        return new_puzzle

    ########################################################
    # Core puzzle methods

    def current_position(self, solved_row, solved_col):
        """
        Locate the current position of the tile that will be at
        position (solved_row, solved_col) when the puzzle is solved
        Returns a tuple of two integers        
        """
        solved_value = (solved_col + self._width * solved_row)

        for row in range(self._height):
            for col in range(self._width):
                if self._grid[row][col] == solved_value:
                    return (row, col)
        assert False, "Value " + str(solved_value) + " not found"

    def update_puzzle(self, move_string):
        """
        Updates the puzzle state based on the provided move string
        """
        zero_row, zero_col = self.current_position(0, 0)
        for direction in move_string:
            if direction == "l":
                assert zero_col > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col - 1]
                self._grid[zero_row][zero_col - 1] = 0
                zero_col -= 1
            elif direction == "r":
                assert zero_col < self._width - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col + 1]
                self._grid[zero_row][zero_col + 1] = 0
                zero_col += 1
            elif direction == "u":
                assert zero_row > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row - 1][zero_col]
                self._grid[zero_row - 1][zero_col] = 0
                zero_row -= 1
            elif direction == "d":
                assert zero_row < self._height - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row + 1][zero_col]
                self._grid[zero_row + 1][zero_col] = 0
                zero_row += 1
            else:
                assert False, "invalid direction: " + direction

    ##################################################################
    # Phase one methods

    def lower_row_invariant(self, target_row, target_col):
        """
        Check whether the puzzle satisfies the specified invariant
        at the given position in the bottom rows of the puzzle (target_row > 1)
        Returns a boolean
        """
        length = target_row * self._width + target_col
        if self.get_number(target_row, target_col) != 0:
            return False
        elif self._width * self._height - length == 1:
            return True
        
        sorted_list = [num for num in range(self._width * self._height)]
        grid_list = []
        for row in range(self._height):
            grid_list += self._grid[row]

        if grid_list[length + 1:] != sorted_list[length + 1:]:
            return False
        return True 

    def find_tile(self, value):
        """
        find the location of the tile corresponding 
        to the specific value
        """
        for row in range(self._height):
            for col in range(self._width):
                if self._grid[row][col] == value:
                    return row, col
                
    def find_num(self, row, col) :
        """
        find the solved number
        corresponding  to col and row
        """
        if row + 1 == self._height and col + 1== self._width:
            return self._height * self._width - 1
        else:
            return self.get_number(row, col + 1) - 1 
    
    def move_tile(self, target_row, target_col, tile_row, tile_col):
        """
        move the tile
        """
        solution = ""
        row_diff = abs(target_row - tile_row)
        col_diff = abs(target_col - tile_col)
        # place tile0 on the same row as target
        solution += "u" * row_diff

        # when tile on tile0 left
        if tile_col < target_col:
            # place tile0 on target left(move left 1 times)
            solution += "l" * col_diff
            # move the target
            for _ in range(col_diff - 1):
                if tile_row == 0:
                    solution += "drrul"
                else:
                    solution += "urrdl"
            # deal with row
            if row_diff > 0:
                # place tile0 on target above(move up 1 times)   
                solution += "dru" 
                
        # when tile on tile0 left
        elif tile_col > target_col:
            # place tile0 on target right(move right 1 times)
            solution += "r" * col_diff                
            # move the target
            for _ in range(col_diff - 1):
                if tile_row == 0:
                    solution += "dllur"
                else:
                    solution += "ulldr"                
            # deal with row
            if row_diff > 0:
                # place tile0 on target above(move up 1 times)   
                solution += "dlu"
                
        for _ in range(row_diff - 1):
            solution += "lddru"                
        # go home             
        if tile_row != target_row:
            solution += "ld"              
        return solution
    
    def solve_interior_tile(self, target_row, target_col):
        """
        Place correct tile at target position
        Updates puzzle and returns a move string
        """
        tile_num = target_row * self._width + target_col
        tile_row, tile_col = self.find_tile(tile_num)
        solution = self.move_tile(target_row, target_col, tile_row, tile_col)
        self.update_puzzle(solution)                
        return solution

    def solve_col0_tile(self, target_row):
        """
        Solve tile in column zero on specified row (> 1)
        Updates puzzle and returns a move string
        """
        solution = "ur"
        if self.get_number(target_row - 1, 0) != self._width * target_row:
            tile_num = self._width * target_row
            self.update_puzzle("ur")
            tile_row, tile_col = self.find_tile(tile_num)
            self.update_puzzle("ld")
            solution += self.move_tile(target_row - 1, 1, tile_row, tile_col)
            solution += "ruldrdlurdluurddlur"
        solution += "r" * (self._width - 2)
        print solution
        self.update_puzzle(solution)
        return solution

    #############################################################
    # Phase two methods

    def row0_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row zero invariant
        at the given column (col > 1)
        Returns a boolean
        """
        num = self.get_number(1, target_col)
        if num == self._width * 1 + target_col:
            self.set_number(1, target_col, 0)
            if self.row1_invariant(target_col) and self.get_number(0, target_col) == 0:
                for col in range(target_col + 1, self._width):
                    if self.get_number(0, col) != col:
                        return False
                return True
            self.set_number(1, target_col, num) 
        return False

    def row1_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row one invariant
        at the given column (col > 1)
        Returns a boolean
        """
        if self.lower_row_invariant(1, target_col):
            for col in range(target_col + 1, self._width):
                if self.get_number(1, col) != self._width * 1 + col:
                    return False
            return True
        return False

    def solve_row0_tile(self, target_col):
        """
        Solve the tile in row zero at the specified column
        Updates puzzle and returns a move string
        """
        solution = "ld"
        if self.get_number(0, target_col - 1) != target_col:
            tile_num = target_col
            self.update_puzzle("ld")
            tile_row, tile_col = self.find_tile(tile_num)
            self.update_puzzle("ur")
            solution += self.move_tile(1, target_col - 1, tile_row, tile_col)
            solution += "urdlurrdluldrruld"
        self.update_puzzle(solution)
        return solution

    def solve_row1_tile(self, target_col):
        """
        Solve the tile in row one at the specified column
        Updates puzzle and returns a move string
        """
        solution = ""
        tile_num = self._width * 1 + target_col
        tile_row, tile_col = self.find_tile(tile_num)
        solution += self.move_tile(1, target_col, tile_row, tile_col)
        solution += "ur"
        self.update_puzzle(solution)
        return solution

    ###########################################################
    # Phase 3 methods

    def solve_2x2(self):
        """
        Solve the upper left 2x2 part of the puzzle
        Updates the puzzle and returns a move string
        """
        solution = ""
        zero_row, zero_col = self.find_tile(0)
        if zero_row == 1:
            solution += "u"
        if zero_col == 1:
            solution += "l"
        self.update_puzzle(solution)
       
        step = "rdlu"
        while self.get_number(0,1) != 1 or self.get_number(1,1) != self._width + 1 or self.get_number(1,0) != self._width:
            solution += step
            self.update_puzzle(step)
        return solution

    def solve_puzzle(self):
        """
        Generate a solution string for a puzzle
        Updates the puzzle and returns a move string
        """
        solution = ""
        
        zero_row, zero_col = self.find_tile(0)
        solution += (self._width - zero_col - 1) * "r"
        solution += (self._height - zero_row - 1) * "d"
        self.update_puzzle(solution)
        
        for row in range(self._height - 1, 1, -1):
            for col in range(self._width - 1, 0, -1):
                solution += self.solve_interior_tile(row, col)
            solution += self.solve_col0_tile(row)
        
        for col in range(self._width - 1, 1, -1):
            solution += self.solve_row1_tile(col)
            solution += self.solve_row0_tile(col)

        solution += self.solve_2x2()
        return solution


# Start interactive simulation
# poc_fifteen_gui.FifteenGUI(Puzzle(4, 4))

## test lower_row_invariant
#obj1 = Puzzle(3, 3, [[8, 7, 6], [5, 4, 3], [2, 1, 0]])
#print obj1
#print obj1.lower_row_invariant(2, 2)
#obj2 = Puzzle(3, 3, [[3, 2, 1], [6, 5, 4], [7, 0, 8]])
#print obj2
#print obj2.lower_row_invariant(2, 1)
#obj = Puzzle(4, 5, [[15, 11, 10, 9, 8], [7, 6, 5, 4, 3], [2, 1, 0, 13, 14], [12, 16, 17, 18, 19]]) 
#print obj
#print obj.lower_row_invariant(2, 2)

#obj = Puzzle(3, 3, [[8, 7, 6], [5, 4, 3], [2, 1, 0]])
#print obj
#print obj.solve_interior_tile(2, 2)
#print obj

#obj = Puzzle(3, 3, [[3, 2, 1], [6, 5, 4], [7, 0, 8]])
#print obj
#print obj.solve_interior_tile(2, 1) 
#print obj


#obj = Puzzle(3, 3, [[3, 2, 1], [6, 5, 4], [0, 7, 8]])
#print obj
#print obj.solve_col0_tile(2)
#print obj


#obj = Puzzle(4, 5, [[12, 11, 10, 9, 15], [7, 6, 5, 4, 3], [2, 1, 8, 13, 14], [0, 16, 17, 18, 19]])
#print obj
#print obj.solve_col0_tile(3)
#print obj


#obj = Puzzle(3, 3, [[4, 3, 2], [1, 0, 5], [6, 7, 8]])
#print obj
#print obj.row1_invariant(1)

#obj = Puzzle(4, 5, [[7, 6, 5, 3, 4], [2, 1, 0, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19]])
#print obj
#print obj.row1_invariant(2)

#obj = Puzzle(3, 3, [[0, 1, 2], [3, 4, 5], [6, 7, 8]])
#print obj
#print obj.row0_invariant(0)

#obj = Puzzle(4, 5, [[7, 2, 0, 3, 4], [5, 6, 1, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19]])
#print obj
#print obj.row0_invariant(2)

#obj = Puzzle(3, 3, [[2, 5, 4], [1, 3, 0], [6, 7, 8]])
#print obj
#print obj.solve_row1_tile(2)
#print obj

#obj = Puzzle(4, 5, [[7, 6, 5, 3, 4], [2, 1, 0, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19]])
#print obj
#print obj.solve_row1_tile(2)
#print obj

#obj = Puzzle(4, 5, [[7, 6, 5, 3, 2], [4, 1, 9, 8, 0], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19]])
#print obj
#print obj.solve_row1_tile(4)
#print obj

#obj = Puzzle(3, 3, [[4, 1, 0], [2, 3, 5], [6, 7, 8]])
#print obj
#obj.solve_row0_tile(2)
#print obj


#obj = Puzzle(4, 5, [[1, 2, 0, 3, 4], [6, 5, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19]])
#print obj
#print obj.solve_row0_tile(2)
#print obj

#obj = Puzzle(3, 3, [[4, 3, 2], [1, 0, 5], [6, 7, 8]])
#print obj
#print obj.solve_2x2()
#print obj


#obj = Puzzle(3, 3, [[8, 7, 6], [5, 4, 3], [2, 1, 0]])
#print obj
#print obj.solve_puzzle()
#print obj

#obj = Puzzle(4, 5, [[15, 16, 0, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [1, 2, 17, 18, 19]])
#print obj
#obj.solve_puzzle()
#print obj
