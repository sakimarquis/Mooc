# coarse-graining games of chess
# a worked example for the SFI Renormalization MOOC
# http://renorm.complexityexplorer.org
# Simon DeDeo / simon@santafe.edu / http://santafe.edu/~simon
# we'll use the python-chess engine; if you're on a Mac, you can install it with
# sudo pip install python-chess
# 
# we'll work with a database of games from
# http://www.pgnmentor.com/files.html

import chess
import chess.pgn
import re # useful for our hacked together coarse-graining via strings
import math

# a single PGN file from pgnmentor contains many games; we'll use Kasparov's oeuvre as an example
pgn = open("Kasparov.pgn")
list=[]
while True:
	game=chess.pgn.read_game(pgn)
	if game == None:
		break
	list.append(game)
## list is now a big list of all of Kasparov's games (in this database)

# let's peek at the board state of the first game
print(str(list[0].board()))
# let's look at the board state after two moves..
print(str(list[0].variation(0).variation(0).board()))

## now we'll define a pair of functions that will allow us to coarse-grain the state of the board at any stage of the game
## the first function takes a 
values={'p': 1, 'n': 3, 'b': 3, 'r': 5, 'q': 9, 'k': 0} ## don't count King
def cg_board(board_string): ## takes the string description of a board (state of the game) and returns the pair of piece values for the two players
	white_count=0
	black_count=0
	for i in board_string:
		str=re.match('[A-Z]', i)
		if str:
			white_count += values[i.lower()]
		str=re.match('[a-z]', i)
		if str:
			black_count += values[i]
	return [white_count, black_count]
 
def cg_board_quad(board_string): ## takes the string description of a board (state of the game) and returns the piece values for each player in each of the four board quadrants
	quad_cg=[]
	for quad in quadrant(board_string):
		quad_cg.append(cg_board(quad))
	return quad_cg

def quadrant(board_string): ## takes the string description of a board (state of the game) and splits it into quadrants
	str_list=board_string.split("\n")
	quad=[]
	for i in range(2):
		for j in range(2):
			str_new=''
			half=str_list[(i*4):(i+1)*4]
			for line in half:
				str_new += line[(j*4)*2:(j+1)*4*2]
			quad.append(str_new)
	return quad

				
## as an example, consider the first game in the Kasparov database
node=list[0]
game_cg_timeseries=[]
game_cg_quad_timeseries=[]
while node.variations:
	next_node = node.variation(0)
	game_cg_timeseries.append(cg_board(str(node.board())))
	game_cg_quad_timeseries.append(cg_board_quad(str(node.board())))
	node = next_node

# game_cg_timeseries and game_cg_quad_timeseries are the coarse-grained timeseries of the game at it advances

## finally, let's compute the entropy of Kasparov's games at the two levels; we'll do this by coarse-graining all of his games, and then just counting the appearances of the different symbols
dict_cg={}
dict_cg_quad={}
running=0
for node in list:
	print(running) ## this takes awhile, so let's print the iteration number so we know it's actually working
	while node.variations:
		next_node = node.variation(0)
		i=str(cg_board(str(node.board()))) ## convert the coarse-grained symbol to a string...
		dict_cg[i] = dict_cg.get(i, 0) + 1 ## ...so that we can use it as a dictionary key (the ".get" method allows us to start counting at zero)
		i=str(cg_board_quad(str(node.board())))
		dict_cg_quad[i] = dict_cg_quad.get(i, 0) + 1
		node = next_node
	running += 1

cg_prob=[dict_cg[i] for i in dict_cg.keys()]
cg_prob_norm=1.0*sum(cg_prob)
sum([-(i/cg_prob_norm)*math.log(i/cg_prob_norm, 2) for i in cg_prob])

cg_prob_quad=[dict_cg_quad[i] for i in dict_cg_quad.keys()]
cg_prob_norm=1.0*sum(cg_prob_quad)
sum([-(i/cg_prob_norm)*math.log(i/cg_prob_norm, 2) for i in cg_prob_quad])





