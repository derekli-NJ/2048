import sys
sys.path.append('../')

from game_logic import Game
from game_logic import has_valid_move
from game_logic import get_empty_squares
import functools

empty_board = [[0, 0, 0, 0],
			   [0, 0, 0, 0],
			   [0, 0, 0, 0],
			   [0, 0, 0, 0]]

test_board = [[0, 0, 2, 2],
			  [0, 2, 0, 0],
			  [0, 0, 2, 0],
			  [2, 0, 2, 2]]

stuck_board = [[2, 4, 2, 4],
			   [4, 8, 4, 2],
			   [8, 4, 2, 8],
			   [2, 8, 4, 2]]

almost_stuck_board_1 = [[2, 4, 2, 4],
						[4, 8, 4, 2],
						[8, 2, 2, 8],
						[2, 8, 4, 2]]

almost_stuck_board_2 = [[2, 4, 2, 4],
						[4, 8, 4, 8],
						[8, 4, 2, 8],
						[2, 8, 4, 2]]

empty_squares = [[0, 0], [0, 1], [1, 0], [1, 2], [1, 3], [2, 0], [2, 1], [2, 3], [3, 1]]

def sum_tiles(board):
	return functools.reduce(lambda x, y: x + sum(y), board, 0)

def test_init(game):
	print("Running test_init...")
	print(game.get_board())
	assert (sum_tiles(game.get_board()) >= 4), "failed __init__(): Did not initialize tiles"
	print("Passed test_init!")

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
	game.board = test_board
	print("Pre:")
	print(game.get_board())
	print("-----")
	tiles_pre = sum_tiles(game.get_board())
	game.spawn_tile()
	print("Post:")
	print(game.get_board())
	new_board = game.get_board()
	tiles_post = sum_tiles(game.get_board())
	assert (tiles_post == tiles_pre + 2) or (tiles_post == tiles_pre + 4), "failed spawn_tile(): Did not increase total tile sum"
	# TODO: more tests
	print("Passed test_spawn_tile!")

def test_get_empty_squares(game):
	print("Running test_get_empty_squares...")
	game.board = test_board
	result = get_empty_squares(game.get_board())

	#TODO: Too lazy to optimize test cases
	for square in result:
		contains = functools.reduce(lambda x, y: x or (y == square), empty_squares, False)
		assert contains, "failed get_empty_squares(): Unexpected output"

	print("Passed test_get_empty_squares!")

def test_has_valid_move(game):
	print("Running test_has_valid_move...")
	game.board = stuck_board
	assert (not has_valid_move(game.get_board())), "failed has_valid_move(): Found valid move for stuck board"
	game.board = test_board
	assert has_valid_move(game.get_board()), "failed has_valid_move(): Could not find move for: test_board"
	game.board = almost_stuck_board_1
	assert has_valid_move(game.get_board()), "failed has_valid_move(): Could not find move for: almost_stuck_board_1"
	game.board = almost_stuck_board_2
	assert has_valid_move(game.get_board()), "failed has_valid_move(): Could not find move for: almost_stuck_board_2"

	print("Passed test_has_valid_move!")

##  
# Run the tests
##
test_game = Game(0, 4)

test_init(test_game)
test_get_board(test_game)
test_clear_board(test_game)
test_spawn_tile(test_game)
test_get_empty_squares(test_game)
test_has_valid_move(test_game)