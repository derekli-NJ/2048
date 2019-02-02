import random

chance_of_4 = 1/12

class Game(object):
    
    def __init__(self, seed):
        random.seed(seed) # TODO: Initialize and store random seeds in a better way
        self.board = [[0,0,0,0],
                          [0,0,0,0],
                          [0,0,0,0],
                          [0,0,0,0]]
        for i in range(0, 2):
            self.spawn_tile()

    def self.get_board(self):
        return self.board
    
    def self.spawn_tile(self):
        
