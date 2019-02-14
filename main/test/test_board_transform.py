import sys
sys.path.append('../')

from board_transform import Move
from board_transform import rotate_move
from board_transform import rotate_board
from boardstates_fortesting import *

def test_rotate_move():
    print("Running test_rotate_move...")
    assert rotate_move(Move.UP) == Move.LEFT
    assert rotate_move(Move.LEFT) == Move.DOWN
    assert rotate_move(Move.DOWN) == Move.RIGHT
    assert rotate_move(Move.RIGHT) == Move.UP

    assert rotate_move(Move.UP, 2) == Move.DOWN
    assert rotate_move(Move.LEFT, 2) == Move.RIGHT
    assert rotate_move(Move.DOWN, 2) == Move.UP
    assert rotate_move(Move.RIGHT, 2) == Move.LEFT

    assert rotate_move(Move.UP, 3) == Move.RIGHT
    assert rotate_move(Move.LEFT, 3) == Move.UP
    assert rotate_move(Move.DOWN, 3) == Move.LEFT
    assert rotate_move(Move.RIGHT, 3) == Move.DOWN

    assert rotate_move(Move.UP, 4) == Move.UP
    assert rotate_move(Move.LEFT, 4) == Move.LEFT
    assert rotate_move(Move.DOWN, 4) == Move.DOWN
    assert rotate_move(Move.RIGHT, 4) == Move.RIGHT

    assert rotate_move(Move.UP, -1) == Move.RIGHT
    assert rotate_move(Move.LEFT, -1) == Move.UP
    assert rotate_move(Move.DOWN, -1) == Move.LEFT
    assert rotate_move(Move.RIGHT, -1) == Move.DOWN

    print("Passed test_rotate_move!")

def test_rotate_board():
    print("Running test_rotate_board...")

    result_board_1 = rotate_board(test_board, 2);
    assert(result_board_1[0]==[4,2,0,0])
    assert(result_board_1[1]==[8,4,4,4])
    assert(result_board_1[2]==[8,2,0,0])
    assert(result_board_1[3]==[4,8,2,0])

    result_board_2 = rotate_board(test_board_2, 2);
    assert(result_board_2[0]==[4,2,0,0])
    assert(result_board_2[1]==[8,4,4,4])
    assert(result_board_2[2]==[8,2,0,0])
    assert(result_board_2[3]==[4,8,2,0])

    print("Passed test_rotate_board!")

test_rotate_move()
test_rotate_board()