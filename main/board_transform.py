from enum import Enum, unique

# Make an enum of moves, @unique to make sure they have different values
@unique
class Move(Enum):
    UP = 0
    LEFT = 1
    DOWN = 2
    RIGHT = 3

def get_all_moves():
    # get all possible moves from above
    return [move.value for move in Move]

def rotate_move(move, amount=1):
	"""
	Rotates a given move by the specified amount. (default 1)
	"""
	return Move((move.value + amount) % 4)

def rotate_board(board, amount=1):
    """
    Rotates the board (2d array) amount times counterclockwise 90 degrees.
    """
    # Only handle inputs from 0-3
    amount = amount % 4

    """
    A few things to note:
    'list(x) for x in zip(*board)' is board_transpose
    '[::-1]' reverses the target list
    """

    # Special casing because there isn't really a point not to
    if amount == 1:
        # Reverse every row, and then flip it 45 degrees.
        return [list(x) for x in zip(*[x[::-1] for x in board])]
    if amount == 2:
        # Reverse the order of rows, then reverse every row.
        return [x[::-1] for x in board][::-1]
    if amount == 3:
        # Reverse the order of rows, then flip it 45 degrees.
        return [list(x) for x in zip(*board[::-1])]
    # if amount == 0:
    return board
