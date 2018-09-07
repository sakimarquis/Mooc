import random
import pylab

# =============================================================================
# ATTENTION!!
# Everytime you run simulation you change the global varialbes
# You must initial the global varialbes after the simulation
# =============================================================================

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30
FOXDIERATE = 1/10
LEASTNUM = 10

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP

    for dummy_rabbit in range(CURRENTRABBITPOP):
        rabbit_reproduction = 1 - (CURRENTRABBITPOP / MAXRABBITPOP)
        if random.random() <= rabbit_reproduction:
            CURRENTRABBITPOP += 1
    
            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    fox_die = 0
    for dummy_fox in range(CURRENTFOXPOP):
        fox_eat = CURRENTRABBITPOP / MAXRABBITPOP
        if CURRENTFOXPOP > LEASTNUM and random.random() <= fox_eat:
            CURRENTRABBITPOP -= 1
            if random.random() <= 1/3:
                CURRENTFOXPOP += 1
        else:
            if random.random() <= FOXDIERATE:
                fox_die += 1

    if CURRENTFOXPOP >= LEASTNUM:
        if CURRENTFOXPOP - fox_die < LEASTNUM:
            CURRENTFOXPOP = LEASTNUM
        else:
            CURRENTFOXPOP -= fox_die
    
            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """
    rabbits = []
    foxes = []
    for _ in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbits.append(CURRENTRABBITPOP)
        foxes.append(CURRENTFOXPOP)
    return rabbits, foxes
    
def plotSimulation():
    numSteps = 200
    rabbits, foxes= runSimulation(numSteps)
    pylab.plot(range(numSteps), rabbits, 'b', label = 'Rabbits') 
    pylab.plot(range(numSteps), foxes, 'r', label = 'Foxes')
    pylab.title("Simulation of foxes and rabbits")
    pylab.xlabel("Timestep")
    pylab.ylabel("Population")
    pylab.legend()
    pylab.show() # plot finish

def plotTwoDegreeFit():
    numSteps = 200
    rabbits, foxes= runSimulation(numSteps)
    coeff_rabbits = pylab.polyfit(range(len(rabbits)), rabbits, 2)
    coeff_foxes = pylab.polyfit(range(len(foxes)), foxes, 2)
    pylab.plot(pylab.polyval(coeff_rabbits, range(len(rabbits))), 'b', label = 'Rabbits')
    pylab.plot(pylab.polyval(coeff_foxes, range(len(foxes))), 'r', label = 'Foxes')
    pylab.title("2nd degree fits of foxes and rabbits")
    pylab.xlabel("Timestep")
    pylab.ylabel("Population")
    pylab.legend() 
    pylab.show() # plot finish


plotSimulation()

MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30
FOXDIERATE = 1/10
LEASTNUM = 10

plotTwoDegreeFit()