# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 00:10:56 2018

@author: saki
"""
def pick_a_number(board): 
    if len(board) == 0:
        return (0, 0)
    else:
        pass


def pick_a_number_wrong(board):   
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

print(pick_a_number([3, 5, 2, 1])
#print(pick_a_number([12, 9, 7, 3, 4, 7, 4, 3, 16, 4, 8, 12, 1, 2, 7, 11, 6, 3, 9, 7, 1]))
#print(pick_a_number_wrong([12, 9, 7, 3, 4, 7, 4, 3, 16, 4, 8, 12, 1, 2, 7, 11, 6, 3, 9, 7, 1]))

