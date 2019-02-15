import sys
sys.path.append('../')

import random
from random_ai import Random_AI
from save_game_data import Save_Game_Data
import copy


def test_Random_AI(random_ai):
    print("Running test_Random_AI...")
    a = [0, 1, 2, 3]

    move = random_ai.get_move()
    assert(a.__contains__(move))


    print("Passed!")

def test_save_game_data(save_game_data):
    print("Running test_save_game_data")

    saveData = save_game_data.save_data()
    board = saveData[0]
    move = saveData[1]
    save_game_data.write_data_to_file()
    print (board)
    print (move)


    assert([[[0, 0, 2, 2], [0, 2, 0, 0], [0, 0, 2, 0], [2, 0, 2, 2]]] == board)


    print("Passed!")


test_board = [[0, 0, 2, 2],
              [0, 2, 0, 0],
              [0, 0, 2, 0],
              [2, 0, 2, 2]]



test_AI = Random_AI(test_board)
test_Random_AI(test_AI)


Save_Game_Data = Save_Game_Data(test_AI)
test_save_game_data(Save_Game_Data)




