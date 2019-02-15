import sys
sys.path.append('../')

from game_data_storage import DataStorage, state_to_string
from boardstates_fortesting import *
from board_transform import Move

def test_state_to_string():
    print("Running test_state_to_string...")
    assert state_to_string(test_board) == "[[0, 0, 2, 2], [0, 2, 0, 0], [0, 0, 2, 0], [2, 0, 2, 2]]", "Somehow failed tostring"
    print("Passed test_state_to_string!")

def test_add_game_data(storage):
    print("Running test_add_game_data...")

    board_list = [test_board, test_board_2]
    moves_list = [Move.UP, Move.DOWN]
    score = 20

    storage.add_game_data(board_list, moves_list, score)

    data = storage.game_list[0].loc[state_to_string(test_board)]

    assert data.name == state_to_string(test_board)

    assert data.loc[Move.UP] == 1
    assert data.loc[Move.LEFT] == 0
    assert data.loc[Move.DOWN] == 0
    assert data.loc[Move.RIGHT] == 0

    print("Passed test_add_game_data!")

storage = DataStorage()

test_state_to_string()
test_add_game_data(storage)