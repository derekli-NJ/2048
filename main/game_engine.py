
# from game_logic import Game
# from random_ai import Random_AI


class GameEngine(object):


    def __init__(self, game_logic, AI):
        self.game_logic = game_logic
        self.AI = random_ai

        # goes from top counter-clockwise
        self.slide_functions = [game_logic.slide_up(), game_logic.slide_left(), game_logic.slide_down(), game_logic.slide_right()]

        

    def run_game(self):


    if event.keysym == "Up":
        print ('Up')
        valid = moveUp(data)
    if event.keysym == "Left":
        print ('Left')
        valid = moveLeft(data)
    if event.keysym == "Right":
        print ('Right')
        valid = moveRight(data)
    if event.keysym == "Down":
        print ('Down')   
        valid = moveDown(data)
    if valid:
        spawn_piece(data)
    if not data.game.has_valid_move():
        data.gameFinished = True










