# My solution
import numpy as np

def is_solved(board):
    lst = np.array(board)
    _all_dim = np.concatenate((lst, lst.transpose(),[np.diagonal(lst)], [np.fliplr(lst).diagonal()]), axis=0)
    unfinished_game = 0

    for row in range(_all_dim.shape[0]):
        elem = set(_all_dim[row, :])
        if {0}.intersection(elem): unfinished_game = 1
        if len(elem) == 1 and list(elem)[0] != 0:
            return list(elem)[0]

    if unfinished_game:
        return -1

    return 0


lst = [[2, 1, 2],
       [0, 1, 2],
       [2, 1, 0]]

is_solved(lst)







