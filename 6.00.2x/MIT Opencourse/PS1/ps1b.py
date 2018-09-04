###########################
# 6.0002 Problem Set 1b: Space Change
# Name:
# Collaborators:
# Time:
# Author: charz, cdenise

#================================
# Part B: Golden Eggs
#================================

# Problem 1

def dp_make_weight(egg_weights, target_weight, memo = {}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.
    
    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)
    
    Returns: int, smallest number of eggs needed to make target weight
    """
    if (len(egg_weights),target_weight) in memo:
        result = memo[(len(egg_weights),target_weight)]
    elif len(egg_weights) == 0 or target_weight == 0:
        result = (float('-inf'), ())
    elif egg_weights[-1] > target_weight:
        result = dp_make_weight(egg_weights[:-1], target_weight, memo)
    else:
        nextItem = egg_weights[-1]
        withNum, withToTake = dp_make_weight(egg_weights, target_weight - nextItem, memo)
        withNum = len(withToTake) + 1
        withoutNum, withoutToTake = dp_make_weight(egg_weights[:-1], target_weight, memo)
        if len(withoutToTake) == 0 or (sum(withToTake)/len(withToTake)) > (sum(withToTake)/len(withoutToTake)):
            result = (withNum, withToTake + (nextItem,))
        else:
            result = (withNum, withoutToTake)            
    memo[(len(egg_weights), target_weight)] = result  
    return result

# EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    egg_weights = (1, 5, 10, 25)
    n = 99
    print("Egg weights = (1, 5, 10, 25)")
    print("n = 99")
    print("Expected ouput: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    print("Actual output:", dp_make_weight(egg_weights, n))
    print()
    
    
# =============================================================================
# Problem B.2
# =============================================================================
"""
1. Explain why it would be difficult to use a brute force algorithm to solve this problem if there
were 30 different egg weights. You do not need to implement a brute force algorithm in order to
answer this.

The complexity of powerset is 2^n. So 30 different egg weights is 1073741824

2. If you were to implement a greedy algorithm for finding the minimum number of eggs
needed, what would the objective function be? What would the constraints be? What strategy
would your greedy algorithm follow to pick which coins to take? You do not need to implement a
greedy algorithm in order to answer this.

Always pick the harviest.

3. Will a greedy algorithm always return the optimal solution to this problem? Explain why it is
optimal or give an example of when it will not return the optimal solution. Again, you do not need
to implement a greedy algorithm in order to answer this.

YES

"""