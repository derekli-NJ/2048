import sys
sys.path.append('../')

from game_logic import Game
import functools

empty_board = [[0, 0, 0, 0],
			   [0, 0, 0, 0],
			   [0, 0, 0, 0],
			   [0, 0, 0, 0]]

test_board = [[0, 0, 2, 2],
			  [0, 2, 0, 0],
			  [0, 0, 2, 0],
			  [2, 0, 2, 2]]

def sum_tiles(board):
	return functools.reduce(lambda x, y: x + sum(y), board, 0)

def test_get_board(game):
	print("Running test_get_board...")
	board = game.get_board()
	assert board, "failed get_board(): null board"
	game.board = test_board
	assert game.get_board() == test_board, "failed get_board(): Wrong board"
	game.board = board
	print("Passed test_get_board!")


def test_clear_board(game):
	print("Running test_clear_board...")
	game.board = test_board
	game.clear_board()
	count = sum_tiles(game.get_board())
	assert count == 0, "failed clear_board(): Board not empty"
	print("Passed test_clear_board!")



def test_spawn_tile(game):
	print("Running test_spawn_tile...")
	game.board = test_board;
	tiles_pre = sum_tiles(game.get_board())
	game.spawn_tile()
	new_board = game.get_board()
	tiles_post = sum_tiles(game.get_board())
	assert (tiles_post == tiles_pre + 2) or (tiles_post == tiles_pre + 4), "failed spawn_tile(): Did not increase total tile sum"
	print("Passed test_spawn_tile!")

##  
# Run the tests
##
test_game = Game(0, 4)

test_get_board(test_game)
test_clear_board(test_game)
test_spawn_tile(test_game)