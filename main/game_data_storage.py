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
        df = pd.DataFrame(index=board_states, columns=tf.Move).fillna(0)
        for state, move in stuff:
            df.loc[state].loc[move] += 1
        self.game_list.append(df)
        self.game_scores.append(final_score)

    def sort_data(self):
        """
        Sorts the list of game scores and game boards by score.
        """

        # zips the game_list and game_Scores, sorts the result by scores, and then puts them back.
        self.game_list, self.game_scores = zip(*sorted(zip(self.game_list, self.game_scores), key=lambda pair: pair[1]))

    def write_data(self, file_path, success_cutoff):
        """
        Writes the game data that is stored in this storage object to the specified file path.
        0 < successCutoff < 1
        successCutoff is the fraction of game states which will recieve a score of 1.
        game states in the lower fraction of scores will recieve a score of -1.
        """
        agg_df = pd.DataFrame(columns=tf.Move)
        for game in self.game_list:
            agg_df = agg_df.add(game, fill_value = 0)
        agg_df.to_csv(file_path)
        pass

    def clear_data(self):
        """
        Removes all the game data from this storage.
        """
        self.game_list.clear()
        self.game_scores.clear()

def state_to_string(board_state):
    """
    Convert a boardstate to a string, for hashing.
    """
    return str(board_state)






    