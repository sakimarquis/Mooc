"""
Mini-max Tic-Tac-Toe Player
"""

import poc_ttt_gui
import poc_ttt_provided as provided

# Set timeout, as mini-max can take a long time
import codeskulptor
codeskulptor.set_timeout(60)

# SCORING VALUES - DO NOT MODIFY
# maximizing X, minimizing O
SCORES = {provided.PLAYERX: 1,
          provided.DRAW: 0,
          provided.PLAYERO: -1}

def mm_move(board, player):
    """
    Make a move on the board.
    
    Returns a tuple with two elements.  The first element is the score
    of the given board and the second element is the desired move as a
    tuple, (row, col).
    """
    # check the current states
    
    # base case
    if board.check_win() == provided.DRAW:
        return SCORES[provided.DRAW], (-1,-1)
    elif board.check_win() != None:
        return SCORES[board.check_win()], (-1,-1)
    
    # recursive case
    else:
        # iterate every possible move, find the max/min value
        max_score = -2
        max_board = []
        max_move = ()
        for move in board.get_empty_squares():
            board_copy = board.clone()
            board_copy.move(move[0], move[1], player)
            # X wins, score +1; O wins,score -1; draw, score 0
            score = mm_move(board_copy, provided.switch_player(player))[0] * SCORES[player]
            # if score == 1,return immediately 
            # or find the max(or min depend on how you computed), always find max in the case
            if score == 1:
                return mm_move(board_copy, provided.switch_player(player))[0],move
            elif score > max_score:
                max_score = score
                max_board = board_copy
                max_move = move
        # return the max found in the loop
        return mm_move(max_board, provided.switch_player(player))[0], max_move

def move_wrapper(board, player, trials):
    """
    Wrapper to allow the use of the same infrastructure that was used
    for Monte Carlo Tic-Tac-Toe.
    """
    move = mm_move(board, player)
    assert move[1] != (-1, -1), "returned illegal move (-1, -1)"
    return move[1]

# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.

# provided.play_game(move_wrapper, 1, False) 
# poc_ttt_gui.run_gui(3, provided.PLAYERO, move_wrapper, 1, False)

#print "move is %s , score is %d, player is %s" % (move,score,"X" if player == 2 else "O")
## test for base case
## draw
#test = provided.TTTBoard(3,board = [[2,3,2],[3,2,3],[3,2,3]])
#print test
#print "draw case",mm_move(test, provided.PLAYERO)
## player = O ,lose and player = X ,win
#test1 = provided.TTTBoard(3,board = [[2,3,2],[3,2,3],[3,2,2]])
#print test1
#print "player = O ,lose", mm_move(test1, provided.PLAYERO)
#print "player = X ,win", mm_move(test1, provided.PLAYERX)
## player = O ,win and player = X ,lose
#test2 = provided.TTTBoard(3,board = [[3,3,2],[3,2,3],[3,2,2]])
#print test2
#print "player = O ,win", mm_move(test2, provided.PLAYERO)
#print "player = X ,lose", mm_move(test2, provided.PLAYERX)

## test 1 move
## draw
#test = provided.TTTBoard(3,board = [[2,3,2],[3,2,3],[3,2,1]])
#print test
#print mm_move(test, provided.PLAYERO)
## player = X ,win
#test = provided.TTTBoard(3,board = [[2,3,2],[3,2,3],[3,2,1]])
#print test
#print mm_move(test, provided.PLAYERX)
#test = provided.TTTBoard(3,board = [[1,3,2],[3,2,3],[3,2,2]])
#print test
#print mm_move(test, provided.PLAYERO)

## test 2 move
#test = provided.TTTBoard(3,board = [[2,3,2],[3,2,3],[3,1,1]])
#print test
#print mm_move(test, provided.PLAYERO)
#print mm_move(test, provided.PLAYERX)
## player = X ,win
#test = provided.TTTBoard(3,board = [[2,3,2],[3,2,3],[1,2,1]])
#print test
#print mm_move(test, provided.PLAYERX)
#print mm_move(test, provided.PLAYERO)
#test = provided.TTTBoard(3,board = [[1,3,2],[3,2,3],[3,2,2]])
#print test
#print mm_move(test, provided.PLAYERO)
