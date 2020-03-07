import numpy as np
from itertools import chain

# Best solution
def is_solved(board):
    b = list(chain(*board))
    for (p, q, r) in [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]:
        if b[p] == b[q] == b[r] != 0:
            return b[p]
    return 0 if 0 in b else -1

# My solution
def is_solved(board):
    lst = np.array(board)
    _all_dim = np.concatenate((lst, lst.transpose(), [np.diagonal(lst)], [np.fliplr(lst).diagonal()]), axis=0)

    for row in range(_all_dim.shape[0]):
        elem = set(_all_dim[row, :])
        if len(elem) == 1 and list(elem)[0] != 0:
            return list(elem)[0]

    if 0 in lst.ravel():
        return -1

    return 0

lst = [[2, 1, 1],
       [1, 1, 0],
       [2, 1, 2]]

is_solved(lst)












