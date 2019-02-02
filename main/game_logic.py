import random
import numpy as np

default_chance_of_4 = 1/15

class Game(object):

    def __init__(self, seed, board_size, four_chance = default_chance_of_4, starting_tiles = 2):
        random.seed(seed) # TODO: Initialize and store random seeds in a better way
        self.board_size = board_size
        self.four_chance = four_chance
        self.board = [([0] * self.board_size) for i in range(self.board_size)]
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
        empty_squares = self.get_empty_squares()
        chosen_square = empty_squares[random.randint(0, len(empty_squares) - 1)]
        next_num = 2
        if random.random() < self.four_chance:
          next_num = 4
        self.get_board()[chosen_square[0]][chosen_square[1]] = next_num
        if len(empty_squares) == 1 and not self.has_valid_move():
            return False
        return True;

    def get_empty_squares(self):
        """
        Finds all the empty tiles in the given board, and returns them in a list
        of (x, y) coordinates.
        """
        empty_squares = [] # List of (row, col) coordinates that are empty in the grid.
        for x, y in np.ndindex((self.board_size, self.board_size)):
            tile = self.board[x][y]
            if tile == 0:
                empty_squares.append([x, y])
        return empty_squares

    def has_valid_move(self):
        """
        Helper function to test if the given board has a valid move.
        """

        for row in range(len(self.board)):
            board = self.board # For convenience
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
