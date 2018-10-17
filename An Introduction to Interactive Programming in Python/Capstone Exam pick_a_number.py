# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 00:10:56 2018

@author: saki
"""


# =============================================================================
# a refine recursive implement adding a memo
# =============================================================================

def pick_a_number(board, memo = dict()): 
    """
    optimal play means that the player maximizes his final score
    """
    if len(board) == 0:
        return (0, 0)
    elif tuple(board) in memo:
        return memo[tuple(board)]
    else:
        memo[tuple(board[1:])] = pick_a_number(board[1:], memo)
        first = board[0] + pick_a_number(board[1:], memo)[1]
        memo[tuple(board[0:-1])] = pick_a_number(board[0:-1], memo)
        last = board[-1] + pick_a_number(board[0:-1], memo)[1]
        if first > last:
            return (first, pick_a_number(board[1:], memo)[0])
        else:
            return (last, pick_a_number(board[0:-1], memo)[0])
       
test = [3, 5, 2, 1]
ans = pick_a_number(test)
print(ans)
board = [12, 9, 7, 3, 4, 7, 4, 3, 16, 4, 8, 12, 1, 2, 7, 11, 6, 3, 9, 7, 1]
ans = pick_a_number(board)
print(ans)

# =============================================================================
# a recursive implement but cost a lot of time
# =============================================================================

def pick_a_number(board): 
    """
    optimal play means that the player maximizes his final score
    """
    if len(board) == 0:
        return (0, 0)
    else:
        first = board[0] + pick_a_number(board[1:])[1]
        last = board[-1] + pick_a_number(board[0:-1])[1]
        if first > last:
            return (first, pick_a_number(board[1:])[0])
        else:
            return (last, pick_a_number(board[0:-1])[0])

#test = [3, 5, 2, 1]
#ans = pick_a_number(test)
#print(ans)
#board = [12, 9, 7, 3, 4, 7, 4, 3, 16, 4, 8, 12, 1, 2, 7, 11, 6, 3, 9, 7, 1]
#ans = pick_a_number(board)
#print(ans)

# =============================================================================
# only compare for a local optimal in two choose
# =============================================================================

def pick_a_number(board): 
    """
    optimal play means that the player maximizes his final score
    """
    if len(board) == 0:
        return (0, None)
    else:
        # optimize the (first take + second take)
        
        first_first = board[0] + pick_a_number(board[2:])[0]
        first_last = board[0] + pick_a_number(board[1:-1])[0]
        first_smaller = min(first_first, first_last)
                
        last_first = board[-1] + pick_a_number(board[1:-1])[0]
        last_last = board[-1] + pick_a_number(board[0:-2])[0]
        last_smaller = min(last_first, last_last)
        
        if first_smaller > last_smaller:
            return (board[0],0)
        else:
            return (board[-1],-1)

def simu_pick(board):
    """
    simulate the pick a number alg
    """
    player1 = []
    player2 = []
    flag = 1
    while len(board) > 0:
        idx = pick_a_number(board)[1]
        if flag == 1:
            player1.append(board.pop(idx))
            flag = 2
        elif flag == 2:
            player2.append(board.pop(idx))
            flag = 1           
    return (player1, player2)

#test = [3, 5, 2, 1]
#ans = simu_pick(test)
#print(ans)
#print(sum(ans[0]), sum(ans[1]))
#board = [12, 9, 7, 3, 4, 7, 4, 3, 16, 4, 8, 12, 1, 2, 7, 11, 6, 3, 9, 7, 1]
#ans = simu_pick(board)
#print(ans)
#print(sum(ans[0]), sum(ans[1]))

# =============================================================================
# initial wrong implement
# doesn't under stand the optimal
# =============================================================================

def pick_a_number(board):
    player1 = []
    player2 = []
    board_copy = board[::]
    turn = 1
    while len(board_copy) > 0:
        first = board_copy[0]
        last = board_copy[-1]
        if first > last:
            best = first
            board_copy.pop(0)
        else:
            best = last
            board_copy.pop(-1)
        if turn == 1:
            player1.append(best)
            turn = 2
        else:
            player2.append(best)
            turn = 1   
    return (sum(player1),sum(player2))

#test = [3, 5, 2, 1]
#ans = pick_a_number(test)
#print(ans)
#board = [12, 9, 7, 3, 4, 7, 4, 3, 16, 4, 8, 12, 1, 2, 7, 11, 6, 3, 9, 7, 1]
#ans = pick_a_number(board)
#print(ans)