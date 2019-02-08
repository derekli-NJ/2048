import random
import numpy as np

default_chance_of_4 = 1/15

class Game(object):

    def __init__(self, seed, board_size, four_chance = default_chance_of_4, starting_tiles = 2):
        random.seed(seed) # TODO: Initialize and store random seeds in a better way
        self.board_size = board_size
        self.four_chance = four_chance
        self.board = [([0] * self.board_size) for i in range(self.board_size)]
        self.score = 0
        for i in range(0, starting_tiles):
            self.spawn_tile()
    

    def get_board(self):
        return self.board


    def clear_board(self):
        """
        Clears the board. (Zeros all the elements.)
        """
        self.board = [([0 * self.board_size]) for i in range(self.board_size)]
    
    def spawn_tile(self):
        """
        Spawns a single tile in this game. Usually 2s, with a chance of 4.
        Picks an empty tile to spawn a new tile in.
        Returns true on success and false on failure.
        """
        empty_squares = get_empty_squares(self.get_board())
        chosen_square = empty_squares[random.randint(0, len(empty_squares) - 1)]
        next_num = 2
        if random.random() < self.four_chance:
            next_num = 4
        self.get_board()[chosen_square[0]][chosen_square[1]] = next_num
        if len(empty_squares) == 1 and not has_valid_move(self.get_board()):
            return False
        return True;


    def check_move_left(self,row):
        """
        Slide a single row of tiles to the left, and return whether any tiles were moved.
        """
        last = 0
        current = 1
        valid = False
        while (current < (self.board_size)):
            #print (self.board[row][current])
            if self.board[row][current] != 0:
                if self.board[row][current] == self.board[row][last]:
                    self.combine(row, current, row, last)
                    last += 1
                    valid = True
                else:
                    if self.board[row][last] != 0:
                        last += 1
                    if current != last:
                        valid = True
                    self.move(row, current, row, last)
            current += 1
        return valid

    def check_move_right(self,row):
        """
        Slide a single row of tiles to the right, and return whether any tiles were moved.
        """
        last = self.board_size - 1
        current = last - 1
        valid = False
        while (current >= 0):
            #print (self.board[row][current])
            if self.board[row][current] != 0:
                if self.board[row][current] == self.board[row][last]:
                    self.combine(row, current, row, last)
                    last -= 1
                    valid = True
                else:
                    if self.board[row][last] != 0:
                        last -= 1
                    if current != last:
                        valid = True
                    self.move(row, current, row, last)
            current -= 1
        return valid

    def check_move_up(self,col):
        """
        Slide a single column of tiles upwards, and return whether any tiles were moved.
        """
        last = 0
        current = 1
        valid = False
        while (current < self.board_size):
            #print (self.board[row][current])
            if self.board[current][col] != 0:
                if self.board[current][col] == self.board[last][col]:
                    self.combine(current, col, last, col)
                    last += 1
                    valid = True
                else:
                    if self.board[last][col] != 0:
                        last += 1
                    if current != last:
                        valid = True
                    self.move(current, col, last, col)
            current += 1
        return valid

    def check_move_down(self,col):
        """
        Slide a single column of tiles downwards, and return whether any tiles were moved.
        """
        last = self.board_size - 1
        current = last - 1
        valid = False
        while (current >= 0):
            #print (self.board[row][current])
            if self.board[current][col] != 0:
                if self.board[current][col] == self.board[last][col]:
                    self.combine(current, col, last, col)
                    last -= 1
                    valid = True
                else:
                    if self.board[last][col] != 0:
                        last -= 1
                    if current != last:
                        valid = True

                    self.move(current, col, last, col)
            current -= 1
        return valid

    def combine(self,pos1_row, pos1_col, pos2_row, pos2_col):
        """
        Add the item in position 1 to the item in position 2. Sets position 1 to zero.
        """
        self.board[pos2_row][pos2_col] += self.board[pos1_row][pos1_col]
        self.board[pos1_row][pos1_col] = 0
        self.score += self.board[pos2_row][pos2_col]
        pass

    def move(self,pos1_row, pos1_col, pos2_row, pos2_col):
        """
        Move the item in position 1 to position 2. (Overwrite) Sets position 1 to zero.
        """
        tmp = self.board[pos1_row][pos1_col]
        self.board[pos1_row][pos1_col] = 0
        self.board[pos2_row][pos2_col] = tmp
        pass


    def slide_left(self):
        valid = False;
        for row in range(self.board_size):
            valid = self.check_move_left(row) or valid
        return valid

    def slide_right(self):
        valid = False;
        for row in range(self.board_size):
            valid = self.check_move_right(row) or valid
        return valid

    def slide_up(self):
        valid = False;
        for col in range(self.board_size):
            valid = self.check_move_up(col) or valid
        return valid

    def slide_down(self):
        valid = False;
        for col in range(self.board_size):
            valid = self.check_move_down(col) or valid
        return valid

    def has_valid_move(self):
        return has_valid_move(self.board)

    def get_score(self):
        return self.score



# Helper functions
def get_empty_squares(board):
    """
    Finds all the empty tiles in the given board, and returns them in a list
    of (x, y) coordinates.
    """
    empty_squares = [] # List of (row, col) coordinates that are empty in the grid.
    for x, y in np.ndindex((len(board), len(board))):
        tile = board[x][y]
        if tile == 0:
            empty_squares.append([x, y])
    return empty_squares

def has_valid_move(board):
    """
    Helper function to test if the given board has a valid move.
    """
    for row in range(len(board)):
        for col in range(len(board)):
            # If an empty space is found, immediately return true
            if board[row][col] == 0:
                return True

            # If not at edge of board:
            if (not row == len(board) - 1) and (board[row][col] == board[row + 1][col]):
                return True # If there are two vertically adjacent matching tiles
            if (not col == len(board) - 1) and (board[row][col] == board[row][col + 1]):
                return True

    return False

