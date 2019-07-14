"""
Student portion of Zombie Apocalypse mini-project
"""

import random
import poc_grid
import poc_queue
import poc_zombie_gui

# global constants
EMPTY = 0 
FULL = 1
FOUR_WAY = 0
EIGHT_WAY = 1
OBSTACLE = 5
HUMAN = 6
ZOMBIE = 7


class Apocalypse(poc_grid.Grid):
    """
    Class for simulating zombie pursuit of human on grid with
    obstacles
    """

    def __init__(self, grid_height, grid_width, obstacle_list = None, 
                 zombie_list = None, human_list = None):
        """
        Create a simulation of given size with given obstacles,
        humans, and zombies
        """
        poc_grid.Grid.__init__(self, grid_height, grid_width)
        if obstacle_list != None:
            for cell in obstacle_list:
                self.set_full(cell[0], cell[1])
        if zombie_list != None:
            self._zombie_list = list(zombie_list)
        else:
            self._zombie_list = []
        if human_list != None:
            self._human_list = list(human_list)  
        else:
            self._human_list = []
        
    def clear(self):
        """
        Set cells in obstacle grid to be empty
        Reset zombie and human lists to be empty
        """
        poc_grid.Grid.clear(self)
        self._zombie_list = []
        self._human_list = []
        
    def add_zombie(self, row, col):
        """
        Add zombie to the zombie list
        """
        self._zombie_list.append((row, col))
                
    def num_zombies(self):
        """
        Return number of zombies
        """
        return len(self._zombie_list)   
          
    def zombies(self):
        """
        Generator that yields the zombies in the order they were
        added.
        """
        for zombie in self._zombie_list:
            yield zombie
            
    def add_human(self, row, col):
        """
        Add human to the human list
        """
        self._human_list.append((row, col))
        
    def num_humans(self):
        """
        Return number of humans
        """
        return len(self._human_list)
    
    def humans(self):
        """
        Generator that yields the humans in the order they were added.
        """
        for human in self._human_list:
            yield human
        
    def compute_distance_field(self, entity_type):
        """
        Function computes and returns a 2D distance field
        Distance at member of entity_list is zero
        Shortest paths avoid obstacles and use four-way distances
        """
        # create two list
        # visited for mark which grid has been computed in distance_field
        create_list = lambda value,width,height: [[value for dummy_col in range(width)]
                            for dummy_row in range(height)]
        visited = create_list(EMPTY, self._grid_width, self._grid_height)
        distance_field = create_list(self._grid_width * self._grid_height, self._grid_width, self._grid_height)

        # determine which entity type, create a queue to load them all
        entity_list = self._zombie_list if entity_type == ZOMBIE else self._human_list
        boundary = poc_queue.Queue()
        # initialize the distance field
        # entity should not be visited ,and it's distance is 0
        for entity in entity_list:
            boundary.enqueue(entity)
            visited[entity[0]][entity[1]] = FULL
            distance_field[entity[0]][entity[1]] = 0
        
        # loop all the grid, bfs
        # from entity to nearest neighbor and next neighbor
        while len(boundary) > 0:
            cell = boundary.dequeue()
            #visited[cell[0]][cell[1]] = FULL
            for neighbor in self.four_neighbors(cell[0], cell[1]):
                if self.is_empty(neighbor[0], neighbor[1]) and visited[neighbor[0]][neighbor[1]] == EMPTY:
                    visited[neighbor[0]][neighbor[1]] = FULL
                    boundary.enqueue(neighbor)
                    distance_field[neighbor[0]][neighbor[1]] = distance_field[cell[0]][cell[1]] + 1
        return distance_field
    
    def move_humans(self, zombie_distance_field):
        """
        Function that moves humans away from zombies, diagonal moves
        are allowed
        """
        for index, human in enumerate(self._human_list):
            a_human_move = []
            can_move = {human:zombie_distance_field[human[0]][human[1]]}
            for neighbor in self.eight_neighbors(human[0], human[1]):
                if self.is_empty(neighbor[0],neighbor[1]):
                    can_move[neighbor] = zombie_distance_field[neighbor[0]][neighbor[1]]                                      
            for key,value in can_move.items():
                if value == max(can_move.values()):
                    a_human_move.append(key)
            self._human_list[index] = random.choice(a_human_move)
    
    def move_zombies(self, human_distance_field):
        """
        Function that moves zombies towards humans, no diagonal moves
        are allowed
        """
        for index, zombie in enumerate(self._zombie_list):
            a_zombie_move = []
            can_move = {zombie:human_distance_field[zombie[0]][zombie[1]]}
            for neighbor in self.four_neighbors(zombie[0], zombie[1]):
                if self.is_empty(neighbor[0],neighbor[1]):
                    can_move[neighbor] = human_distance_field[neighbor[0]][neighbor[1]] 
            for key,value in can_move.items():
                if value == min(can_move.values()):
                    a_zombie_move.append(key)
            self._zombie_list[index] = random.choice(a_zombie_move)
            
# Start up gui for simulation - You will need to write some code above
# before this will work without errors

# poc_zombie_gui.run_gui(Apocalypse(30, 40))
#test = Apocalypse(2,2)
#test.add_zombie(0,0)
#test.add_zombie(1,1)
#test.add_zombie(3,3)
#test.add_human(0,0)
#test.add_human(3,3)
#t1 = test.compute_distance_field(ZOMBIE)
#t2 = test.compute_distance_field(HUMAN)
#print test.compute_distance_field(ZOMBIE)
#print test.compute_distance_field(HUMAN)
#test.move_humans(t1)
#test.move_zombies(t1)
#print test.compute_distance_field(HUMAN)
#print test.compute_distance_field(ZOMBIE)

#obj = Apocalypse(3, 3, [(0, 0), (0, 1), (0, 2), (1, 0)], [(2, 1)], [(1, 1)])
#print obj
#dist = [[9, 9, 9], [9, 1, 2], [1, 0, 1]]
#print obj.humans().next()
#print dist
#obj.move_humans(dist) 
#print obj.humans().next()

#then obj.humans() expected location to be one of [(1, 2)] but received (1, 0)
