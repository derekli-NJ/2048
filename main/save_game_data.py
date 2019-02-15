

class Save_Game_Data(object):

    def __init__(self, AI):
        # self.boardState = []
        # self.moveChoice = moveChoice

        self.boardState = AI.get_game_board()
        self.moveChoice = AI.get_move_choice()
        
        self.boardStateSave = []
        self.moveMade = []

        self.pathname = "../GameData/Test.txt"
        self.txtFile = open(self.pathname, "a") 
        self.readTxtFile = open(self.pathname, "r")

    def save_data(self):
        

        self.boardStateSave.append(self.boardState)
        self.moveMade.append(self.moveChoice)


        return (self.boardStateSave, self.moveMade)


    def write_data_to_file(self):
        self.txtFile.write("HELLO JINGCHEN")
    
        self.readTxtFile = open(self.pathname, "r")


        for line in self.readTxtFile:
            print (line)
        pass