from tkinter import *
import random

chance_of_4 = 1/12

def init(data):
    initBoard = [[0,0,0,0],
                 [0,0,0,0],
                 [0,0,0,0],
                 [0,0,0,0]]
    data.gameBoard = createStartBoard(initBoard)
    data.row = len(data.gameBoard)
    data.col = len(data.gameBoard[0])
    data.width = 400
    data.height = 400


def printBoard(initBoard):
    for row in range(len(initBoard)):
        print (initBoard[row])

def createStartBoard(initBoard):
    # uses board of all 0's and creates the starting board with 2 pieces
    for i in range(2):
        randRow = random.randint(0,len(initBoard)-1)
        randCol = random.randint(0,len(initBoard[0])-1)
        if initBoard[randRow][randCol] == 0:
            if i == 0:
                initBoard[randRow][randCol] = 2
            else:
                initBoard[randRow][randCol] = random.choice([2,4])
    return initBoard

def createPiece(data):
    ret = data.gameBoard.copy()
    remainingSpots = []
    for row in range(0, ret.row):
        for col in range(0, ret.col):
            if data.gameBoard[row][col]==0:
                lastRow = row
                lastCol = col
                remainingSpots+=[row, col]
                if remainingSpots >= 1:
                    break
    if remainingSpots == 0:
        return False
    if remainingSpots == 1:
        data.gameBoard[lastRow][lastCol] = random.choice([2,4])
        if isLegal(data):
            pass    
        else:
            print('You Lost!')
        # data.gameOver = True
    else:
        newPiece = True
        while newPiece:
            randRow = random.randint(0,data.row-1)
            randCol = random.randint(0,data.col-1)
            if data.gameBoard[randRow][randCol]==0:
                data.gameBoard[randRow][randCol] = random.choice([2,4])
                newPiece = False

def moveUp(data):
    for col in range(0,data.col):
        if data.gameBoard[0][col] == 0:
            for row in range(0,data.row):
                if data.gameBoard[row][col] != 0:
                    data.gameBoard[0][col] = data.gameBoard[row][col]
                    data.gameBoard[row][col] = 0

def moveLeft(data):
    for row in range(0,data.row):
        if data.gameBoard[row][0] == 0:
            for col in range(0,data.col):
                if data.gameBoard[row][col] != 0:
                    data.gameBoard[row][0] = data.gameBoard[row][col]
                    data.gameBoard[row][col] = 0

def moveRight(data):
    for row in range(0,data.row):
        if data.gameBoard[row][data.col-1] == 0:
            for col in range(0,data.col):
                if data.gameBoard[row][col] != 0:
                    data.gameBoard[row][data.col-1] = data.gameBoard[row][col]
                    data.gameBoard[row][col] = 0

def moveDown(data):
    for col in range(0,data.col):
        if data.gameBoard[data.row-1][col] == 0:
            for row in range(0,data.row):
                if data.gameBoard[row][col] != 0:
                    print (row,col)
                    data.gameBoard[data.row-1][col] = data.gameBoard[row][col]
                    if data.gameBoard[data.row-1][col] == 0:
                        data.gameBoard[row][col] = 0
    print (data.gameBoard)

def isLegal(data):
    for row in range(0,data.row):
        for col in range(0,data.col):
            if data.gameBoard[row][col]!=0:
                for num in range(-1,2):
                    if data.gameBoard[row][col]!=data.gameBoard[row+num][col] and data.gameBoard[row][col]!=data.gameBoard[row][col+num]:
                        return False
    return True

                

def runGame():
    printBoard(init())


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
    data.gameBoard = createPiece(data)
    isLegal(data)



def drawGameBoard(canvas,data):
    # draws gameboard
    canvas.create_rectangle(0,0,data.width,data.height,fill = 'gray')
    for row in range(data.row):
        canvas.create_line(0,data.height*(row/4),
                           data.width,data.height*(row/4),width = 5, fill = 'black')
        for col in range(data.col):
            canvas.create_line(data.width * (col/4),
                               0,data.width * (col/4),data.height,width = 5, fill = 'black')
            if col < data.col and row <data.row:
                canvas.create_text(data.width * ((2*col+1)/8),data.height * ((2*row+1)/8),
                                   text = str(data.gameBoard[row][col]), font = ("Avenir",40))


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


