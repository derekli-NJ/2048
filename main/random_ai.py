import random


class Random_AI(object):

    def __init__(self, board):
        self.board = board
        self.moves = ["Left","Right","Up","Down"]
        # self.checkMoves = [game.check_move_up()]
        self.boardState = []
        self.moveMade = []
        pass

    # save board states and moves and final score


    def save_game_data(self):
        self.boardState.append(self.board)
        self.moveMade.append(self.get_random_move())
        return (self.boardState, self.moveMade)

    def get_random_move(self):
        foundValidMove = False
        # while (foundValidMove):
        moveInd = random.randint(0,len(self.moves) - 1)
        # has_valid_move(game.get_board())
        moveChoice = self.moves[moveInd]
        return moveChoice

    def get_move_priorities():
        pass












