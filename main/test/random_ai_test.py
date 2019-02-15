import sys
sys.path.append('../')

import random
from random_ai import Random_AI
import copy


def test_Random_AI(random_ai):
    print("Running test_Random_AI...")
    a = [0, 1, 2, 3]

    move = random_ai.get_move()
    assert(a.__contains__(move))


    print("Passed!")


test_board = [[0, 0, 2, 2],
              [0, 2, 0, 0],
              [0, 0, 2, 0],
              [2, 0, 2, 2]]



test_AI = Random_AI(test_board)
test_Random_AI(test_AI)




