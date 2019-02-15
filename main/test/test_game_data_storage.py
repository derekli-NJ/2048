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

    board_list = [state_to_string(x) for x in board_list]

    storage.add_game_data(board_list, moves_list, score)

    data = storage.game_list[0].loc[board_list[0]]

    assert data.name == state_to_string(test_board)

    assert data.loc[Move.UP] == 1
    assert data.loc[Move.LEFT] == 0
    assert data.loc[Move.DOWN] == 0
    assert data.loc[Move.RIGHT] == 0

    print("Passed test_add_game_data!")
    storage.clear_data()

def test_sort_data(storage):
    print("Running test_sort_data...")

    game_board1 = [state_to_string(test_board)]
    game_moves1 = [Move.UP]
    game_score1 = 5
    game_board2 = [state_to_string(test_board_2)]
    game_moves2 = [Move.RIGHT]
    game_score2 = 15
    game_board3 = [state_to_string(stuck_board)]
    game_moves3 = [Move.DOWN]
    game_score3 = 70
    game_board4 = [state_to_string(almost_stuck_board_1)]
    game_moves4 = [Move.LEFT]
    game_score4 = 7

    storage.add_game_data(game_board1, game_moves1, game_score1)
    storage.add_game_data(game_board2, game_moves2, game_score2)
    storage.add_game_data(game_board3, game_moves3, game_score3)
    storage.add_game_data(game_board4, game_moves4, game_score4)

    storage.sort_data()

    games = storage.game_list
    assert(games[0].iloc[0].name == state_to_string(test_board))
    assert(games[1].iloc[0].name == state_to_string(almost_stuck_board_1))
    assert(games[2].iloc[0].name == state_to_string(test_board_2))
    assert(games[3].iloc[0].name == state_to_string(stuck_board))

    scores = storage.game_scores
    assert scores[0] == 5
    assert scores[1] == 7
    assert scores[2] == 15
    assert scores[3] == 70

    assert len(games) == 4
    assert len(scores) == 4

    print("Passed test_sort_data!")

def test_write_data(storage):
    print("Running test_write_data...")
    storage.write_data("../GameData/Test2.csv", 0.5)

    print("Passed test_write_data!")

storage = DataStorage()

test_state_to_string()
test_add_game_data(storage)
test_sort_data(storage)
test_write_data(storage)