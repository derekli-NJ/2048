empty_board = [[0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0]]

test_board = [[0, 0, 2, 2],
              [0, 2, 0, 0],
              [0, 0, 2, 0],
              [2, 0, 2, 2]]
# Empty squares in test_board
empty_squares = [[0, 0], [0, 1], [1, 0], [1, 2], [1, 3], [2, 0], [2, 1], [2, 3], [3, 1]]

test_board_2 = [[0, 2, 8, 4],
                [0, 0, 2, 8],
                [4, 4, 4, 8],
                [0, 0, 2, 4]]

stuck_board = [[2, 4, 2, 4],
               [4, 8, 4, 2],
               [8, 4, 2, 8],
               [2, 8, 4, 2]]

almost_stuck_board_1 = [[2, 4, 2, 4],
                        [4, 8, 4, 2],
                        [8, 2, 2, 8],
                        [2, 8, 4, 2]]

almost_stuck_board_2 = [[2, 4, 2, 4],
                        [4, 8, 4, 8],
                        [8, 4, 2, 8],
                        [2, 8, 4, 2]]