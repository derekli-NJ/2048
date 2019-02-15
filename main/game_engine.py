
# from game_logic import Game
import game_logic
# from random_ai import Random_AI
from game_data_storage import state_to_string

class Game_Engine(object):


    def __init__(self, gameLogic, AI):
        self.gameLogic = gameLogic
        self.AI = AI
        self.moveChoice = None
        self.hasValidMoves = True
        self.validMove = False
        self.boardStates = []
        self.movesMade = []
        # goes from top counter-clockwise
        self.slide_functions = [gameLogic.slide_up, gameLogic.slide_left, gameLogic.slide_down, gameLogic.slide_right]

        
    def get_board_states(self):
        return self.boardStates

    def get_moves_made(self):
        return self.movesMade

    def run_game(self):
        # runs individual game
        while (self.hasValidMoves == True):
            self.boardStates.append(state_to_string(self.gameLogic.get_board()))
            moveChoice = self.AI.get_move(self.gameLogic.get_board())
            self.movesMade.append(moveChoice)

            self.validMove = self.slide_functions[moveChoice]()
            if self.validMove:
                self.validMove
                self.gameLogic.spawn_tile()
            elif (not game_logic.has_valid_move(self.gameLogic.get_board())):
                self.hasValidMoves = False
        # record and then clear when done
    

    def run_multiple_games(self, gameCount):
        count = 0
        while (count < gameCount):
            run_game()
            count += 1













