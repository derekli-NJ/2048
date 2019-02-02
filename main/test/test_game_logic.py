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
	print("Passed test_spawn_tile!")

def test_get_empty_squares(game):
	print("Running test_get_empty_squares...")
	game.board = test_board
	result = game.get_empty_squares(game.get_board())

	#TODO: Too lazy to optimize test cases
	for square in result:
		contains = functools.reduce(lambda x, y: x or (y == square), empty_squares, False)
		assert contains, "failed get_empty_squares(): Unexpected output"

	print("Passed test_get_empty_squares!")

##  
# Run the tests
##
test_game = Game(0, 4)

test_init(test_game)
test_get_board(test_game)
test_clear_board(test_game)
test_spawn_tile(test_game)
test_get_empty_squares(test_game)