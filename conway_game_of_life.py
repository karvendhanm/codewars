from itertools import chain
import numpy as np

def form_quotient_remainder_dict(num):
    _q_r_dict = {}
    for idx in range(num**2):
        _q_r_dict[idx] = [idx//num, idx%num]
    return _q_r_dict

def is_acceptable_cell(lst1, lst2):
    _bool = False
    if (abs(lst1[0] - lst2[0]) <= 1) & (abs(lst1[1] - lst2[1]) <= 1):
        if (abs(lst1[0] - lst2[0]) > 0) | (abs(lst1[1] - lst2[1]) > 0):
            _bool = True
    return _bool

def form_acceptable_cells_dict(num, _dict):
    _acceptable_cells_dict = {}
    for idx in range(num**2):
        lst = []
        for jdx in range(num**2):
            if is_acceptable_cell(_dict[idx], _dict[jdx]):
                lst.append(jdx)
        _acceptable_cells_dict[idx] = lst
    return _acceptable_cells_dict

def num_of_live_neigbours(shape, array, row, col):
    _dict = form_quotient_remainder_dict(shape)
    __acceptable_cells_dict = form_acceptable_cells_dict(shape, _dict)
    _lst = np.array(list(chain(*array)))
    _req_cells = __acceptable_cells_dict[row*shape + col]
    return sum(_lst[_req_cells])



def get_generation(cells, generations):
    cells = np.array(cells)
    arr = cells.copy()
    for idx in range(generations):
        for row in range(3):
            for col in range(3):
                _live = num_of_live_neigbours(3, cells, row, col)
                if (_live < 2) | (_live > 3):
                    arr[row, col] = 0
                elif (_live == 3) & (arr[row, col] == 0):
                    arr[row, col] = 1
        cells = arr.copy()
    return cells.tolist()

lst = [[1, 0, 0],
       [0, 1, 1],
       [1, 1, 0]]

cells = get_generation(lst, 1)
print(cells)


