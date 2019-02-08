


class Save_Game_Data(object):

    def __init__(self, AI):
        # self.boardState = []
        # self.moveChoice = moveChoice

        self.boardState = AI.get_game_board()
        self.moveChoice = AI.get_move_choice()

        self.boardStateSave = []
        self.moveMade = []


    def save_data(self):
        

        self.boardStateSave.append(self.boardState)
        self.moveMade.append(self.moveChoice)


        return (self.boardStateSave, self.moveMade)







