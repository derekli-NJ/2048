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
    amount = amount % 4
    if amount == 2:
        return list(x[::-1] for x in board)[::-1]
    return board
