import pandas as pd
import board_transform as tf

class DataStorage(object):

    """
    Dataframe structure:

    First column: Board states
    Columns 2-5: Moves (up, down, left, right)
    """

    def __init__(self):
        self.game_list = [] # List of dataframes
        self.game_scores = [] # List of scores

    """
    Add a game's worth of data to this storage.

    board_states: list of board states.
    move: list of moves, 1:1 with board states.
    final_score: final score.
    """
    def add_game_data(self, board_states, moves, final_score):
        # TODO: get moves properly
        stuff = zip(board_states, moves)
        df = ps.DataFrame(index=board_states, columns=tf.Move)
        pass