"""
A simple recursive solver for Nim
http://en.wikipedia.org/wiki/Nim#The_21_game
"""


MAX_REMOVE = 3

# recursive solver with no memoization


def evaluate_position(current_num):
    """
    Recursive solver for Nim
    """
    global counter
    counter += 1

    if current_num == 0:
        return "lost"
    elif current_num <= MAX_REMOVE:
        return "won"
    for remove in range(1, min(MAX_REMOVE, current_num) + 1):
        if evaluate_position(current_num - remove) == "lost":
            return "won"
    return "lost"


def run_standard(items):
    """
    Encapsulate code to run regular recursive solver
    """
    global counter
    counter = 0
    print
    print "Standard recursive version"
    print "Position with", items, "items is", evaluate_position(items)
    print "Evaluated in", counter, "calls"

run_standard(21)


# memoized version with dictionary

def evaluate_memo_position(current_num, memo_dict):
    """
    Memoized version of evaluate_position
    memo_dict is a dictionary that stores previously computed results
    """
    global counter
    counter += 1

    if current_num in memo_dict:
        return memo_dict[current_num]

    for remove in range(1, min(MAX_REMOVE, current_num) + 1):
        memo_dict[current_num - remove] = evaluate_memo_position(current_num - remove, memo_dict)
        if memo_dict[current_num - remove] == "lost":
            return "won"
    return "lost"


def run_memoized(items):
    """
    Run the memoized version of the solver
    """
    global counter
    counter = 0
    print
    print "Memoized version"
    print "Position with", items, "items is", evaluate_memo_position(items, {0 : "lost"})
    print "Evaluated in", counter, "calls"
    
run_memoized(21)
