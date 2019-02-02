from tkinter import *
from game_logic import Game
import sys

def init(data):
    data.game = Game(0, 4)
    data.width = 400
    data.height = 400

def spawn_piece(data):
    data.game.spawn_piece()

def moveUp(data):
    pass

def moveLeft(data):
    pass

def moveRight(data):
    pass

def moveDown(data):
    # for col in range(0,data.col):
    #     if data.gameBoard[data.row-1][col] == 0:
    #         for row in range(0,data.row):
    #             if data.gameBoard[row][col] != 0:
    #                 print (row,col)
    #                 data.gameBoard[data.row-1][col] = data.gameBoard[row][col]
    #                 if data.gameBoard[data.row-1][col] == 0:
    #                     data.gameBoard[row][col] = 0
    # print (data.gameBoard)
    pass

def isLegal(data):
    for row in range(0,data.row):
        for col in range(0,data.col):
            if data.gameBoard[row][col]!=0:
                for num in range(-1,2):
                    if data.gameBoard[row][col]!=data.gameBoard[row+num][col] and data.gameBoard[row][col]!=data.gameBoard[row][col+num]:
                        return False
    return True

                
# TODO ???
def runGame():
    pass


def mousePressed(event,data):
    pass

def keyPressed(event,data):
    if event.keysym == "Up":
        print ('Up')
        moveUp(data)
    if event.keysym == "Left":
        print ('Left')
        moveLeft(data)
    if event.keysym == "Right":
        print ('Right')
        moveRight(data)
    if event.keysym == "Down":
        moveDown(data)
        print ('Down')   
    data.game = spawn_piece(data)
    if not data.game.has_valid_move():
        sys.exit()


def drawGameBoard(canvas,data):
    # draws gameboard
    canvas.create_rectangle(0,0,data.width,data.height,fill = 'gray')
    game_board = data.game.get_board()
    for row in range(len(game_board)):
        canvas.create_line(0,data.height*(row/4),
                           data.width,data.height*(row/4),width = 5, fill = 'black')
        for col in range(len(game_board)):
            canvas.create_line(data.width * (col/4),
                               0,data.width * (col/4),data.height,width = 5, fill = 'black')
            #if col < data.col and row <data.row:
            canvas.create_text(data.width * ((2*col+1)/8),data.height * ((2*row+1)/8),
                                   text = str(game_board[row][col]), font = ("Avenir",40))


def redrawAll(canvas,data):
    # drawStartScreen(canvas,data)
    drawGameBoard(canvas,data)


####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    # def timerFiredWrapper(canvas, data):
    #     timerFired(data)
    #     redrawAllWrapper(canvas, data)
    #     # pause, then call timerFired again
    #     canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    init(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    # timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")



run(width = 400, height = 400)


