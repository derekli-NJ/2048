import sys
sys.path.append('../')


from game_engine import Game_Engine
from game_logic import Game
from random_ai import Random_AI



def test_game_engine(game_engine):
    game_engine.run_game()
    print (game_engine.get_board_states())
    print (game_engine.get_moves_made())










test_game = Game(0, 4)

test_AI = Random_AI()
game_engine = Game_Engine(test_game, test_AI)
test_game_engine(game_engine)


