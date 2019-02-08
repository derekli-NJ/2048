from abc import ABC, abstractmethod
from enum import Enum

class AI(object):

	def __init__(self):
		pass

	@abstractmethod
	def get_move_priorities(self, board):
		pass


class Move(Enum):
	