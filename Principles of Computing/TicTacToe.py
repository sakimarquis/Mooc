"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 100        # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player


def mc_trial(board, player):
    '''
    This function takes a current board and the next player
    to move. The function should play a game starting with 
    the given player by making random moves, alternating 
    between players.The function modifies the board input.
    '''
    while len(board.get_empty_squares()) > 0 and board.check_win() == None:
        row, col = random.choice(board.get_empty_squares())
        board.move(row, col, player)
        player = provided.switch_player(player)

def mc_update_scores(scores, board, player):
    '''
    This function takes a grid of scores (a list of lists)
    with the same dimensions as the Tic-Tac-Toe board.
    The function scores the completed board and update the scores grid. 
    '''
    if board.check_win() != provided.DRAW:
        if player == board.check_win():
            para = 1
        else:
            para = -1
        for row in range(board.get_dim()):
            for col in range(board.get_dim()):
                if board.square(row,col) == player:
                    scores[row][col] = scores[row][col] + para * SCORE_CURRENT
                elif board.square(row,col) == provided.EMPTY:
                    scores[row][col] += 0
                else:
                    scores[row][col] = scores[row][col] - para * SCORE_OTHER
                    
def get_best_move(board,scores):
    '''
    This function takes a current board and a grid of 
    scores. The function finds all of the empty squares 
    with the maximum score and randomly return one of 
    them as a (row,column) tuple.
    '''
    index = []
    empty_dict = {}
    if len(board.get_empty_squares()) > 0:
        empty_list = board.get_empty_squares()
        for loc in empty_list:
            empty_dict[loc] = scores[loc[0]][loc[1]]
        for key, value in empty_dict.items():
            if value == max(empty_dict.values()):
                index.append(key)
        return tuple(random.choice(index))

def mc_move(board,player,trials):
    '''
    This function takes a current board, which player the 
    machine player is, and the number of trials to run, 
    returns a move for the machine player in the form of 
    a (row,column) tuple. 
    '''
    count = 0
    scores = [[0 for dummycol in range(board.get_dim())] for dummyrow in range(board.get_dim())]
    while count < trials:
        board_copy = board.clone()
        mc_trial(board_copy, player)
        mc_update_scores(scores, board_copy, player)
        count += 1
    return get_best_move(board,scores)


# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

#provided.play_game(mc_move, NTRIALS, False)        
poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
