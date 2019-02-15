import pandas as pd
import board_transform as tf

class DataStorage(object):

    """
    Dataframe structure:

    Indices: Board states
    Columns 1-4: Moves (up, down, left, right)
    """

    def __init__(self):
        self.game_list = [] # List of dataframes
        self.game_scores = [] # List of scores


    def add_game_data(self, board_states, moves, final_score):
        """
        Add a game's worth of data to this storage.

        board_states: list of board states.
        move: list of moves, 1:1 with board states.
        final_score: final score.
        """
        stuff = zip(board_states, moves)
        df = pd.DataFrame(index=(state_to_string(x) for x in board_states), columns=tf.Move).fillna(0)
        for state, move in stuff:
            df.loc[state_to_string(state)].loc[move] = 1
        self.game_list.append(df)
        self.game_scores.append(moves)
        pass

    def sort_data(self):
        """
        Sorts the list of game scores and game boards by score.
        """

        # zips the game_list and game_Scores, sorts the result by scores, and then puts them back.
        self.game_list, self.game_scores = sorted(zip(self.game_list, self.game_scores), key=lambda pair: pair[1])


def state_to_string(board_state):
    """
    Convert a boardstate to a string, for hashing.
    """
    return str(board_state)






    