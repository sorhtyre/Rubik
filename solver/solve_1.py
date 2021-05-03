'''Rubik's solver functions'''

from data.cube import pieces
from solver.si import do_move, do_seq


def find_solution():
    '''Find solution'''

    tmp_pieces = [['W', 'R'], ['W', 'O'], ['W', 'B'], ['W', 'G']]

    find_fcenter()
    find_ncenter()

    find_1(find_piece(tmp_pieces[0]))
    find_2(find_piece(tmp_pieces[1]))
    find_3(find_piece(tmp_pieces[2]))
    find_4(find_piece(tmp_pieces[3]))

    return(pieces[1] == 'W' and pieces[16] == 'G' and
           pieces[7] == 'W' and pieces[28] == 'B' and
           pieces[5] == 'W' and pieces[48] == 'O' and
           pieces[3] == 'W' and pieces[41] == 'R')


def find_piece(t_piece):
    '''Find pience'''

    tmp_mids = [[1, 16],  [3, 41],  [5, 48],  [7, 28],  [10, 25], [12, 37],
                [14, 46], [19, 34], [21, 39], [23, 50], [30, 43], [32, 52]]

    for w_items in tmp_mids[:]:
        if t_piece[0] in [pieces[w_items[0]],
                          pieces[w_items[1]]]:
            if t_piece[1] in [pieces[w_items[0]],
                              pieces[w_items[1]]]:
                return w_items
    return None


def find_fcenter():
    '''Find first center'''

    if pieces[4] != 'W':

        if pieces[13] == 'W':
            do_move('SD')

        elif pieces[22] == 'W':
            do_move('SD')
            do_move('SD')

        elif pieces[31] == 'W':
            do_move('SU')

        elif pieces[40] == 'W':
            do_move('SR')

        elif pieces[49] == 'W':
            do_move('SL')


def find_ncenter():
    '''Find next center'''

    if pieces[13] != 'G':

        if pieces[31] == 'G':
            do_move('RR')
            do_move('RR')

        elif pieces[40] == 'G':
            do_move('RR')

        elif pieces[49] == 'G':
            do_move('RL')


def find_1(center_left):
    '''Find 1'''

    pos = {
        1:  ['11'],
        3:  [],
        5:  ['11', '11'],
        7:  ['12'],
        10: ['2', '6'],
        12: ['6'],
        14: ['8', '11', '11'],
        16: ['1', '6'],
        19: ['4', '4', '12'],
        21: ['6', '6'],
        23: ['9', '9', '6', '6'],
        25: ['2', '2', '11'],
        28: ['3', '5'],
        30: ['5'],
        32: ['7', '11', '11'],
        34: ['4', '5'],
        37: ['2', '11'],
        39: ['5', '4', '12'],
        41: ['6', '4', '12'],
        43: ['4', '12'],
        46: ['1', '11'],
        48: ['7', '1', '11'],
        50: ['7', '3', '12'],
        52: ['3', '12']
    }

    for tmp_item in center_left:
        if pieces[tmp_item] == 'W':
            do_seq(pos[tmp_item])
            break


def find_2(center_right):
    '''Find 2'''

    pos = {
        1:  ['2', '2', '10', '8', '8'],
        3:  [],
        5:  [],
        7:  ['4', '4', '9', '8', '8'],
        10: ['1', '8'],
        12: ['1', '1', '8'],
        14: ['8'],
        16: ['2', '8'],
        19: ['9', '8', '8'],
        21: ['9', '9', '8', '8'],
        23: ['8', '8'],
        25: ['10', '8', '8'],
        28: ['4', '7'],
        30: ['4', '4', '7'],
        32: ['7'],
        34: ['3', '7'],
        37: ['1', '10', '8', '8'],
        39: ['10', '1', '8'],
        41: [],
        43: ['3', '9', '8', '8'],
        46: ['2', '10', '8', '8'],
        48: ['8', '4', '9', '8', '8'],
        50: ['10', '3', '7'],
        52: ['8', '9', '1', '8']
    }

    for tmp_item in center_right:
        if pieces[tmp_item] == 'W':
            do_seq(pos[tmp_item])
            break


def find_3(center_bottom):
    '''Find 3'''

    pos = {
        1:  ['1', '1', '10', '10', '3', '3'],
        3:  [],
        5:  [],
        7:  [],
        10: ['10', '7', '3', '8'],
        12: ['1', '10', '7', '3', '8'],
        14: ['2', '10', '7', '3', '8'],
        16: ['1', '1', '10', '7', '3', '8'],
        19: ['3', '3'],
        21: ['9', '3', '3'],
        23: ['10', '3', '3'],
        25: ['9', '9', '3', '3'],
        28: ['7', '4', '8', '10', '3', '3'],
        30: ['7', '3', '3', '8', '10', '3', '3'],
        32: ['8', '10', '7', '3', '3'],
        34: ['8', '9', '7', '3'],
        37: ['1', '10', '10', '3', '3'],
        39: ['5', '4', '6'],
        41: [],
        43: ['4'],
        46: ['7', '7', '3', '8', '8'],
        48: [],
        50: ['7', '3', '8'],
        52: ['3']
    }

    for tmp_item in center_bottom:
        if pieces[tmp_item] == 'W':
            do_seq(pos[tmp_item])
            break


def find_4(center_top):
    '''Find 4'''

    pos = {
        1:  [],
        3:  [],
        5:  [],
        7:  [],
        10: ['10', '8', '1', '7'],
        12: ['11', '6', '12'],
        14: ['12', '8', '11'],
        16: ['12', '7', '11', '1'],
        19: ['10', '10', '1', '1'],
        21: ['10', '1', '1'],
        23: ['9', '2', '2'],
        25: ['1', '1'],
        28: [],
        30: ['11', '5', '12'],
        32: ['12', '7', '11'],
        34: ['7', '9', '8', '1'],
        37: ['2'],
        39: ['11', '6', '12', '2'],
        41: [],
        43: ['11', '6', '6', '12', '2'],
        46: ['1'],
        48: [],
        50: ['12', '8', '11', '1'],
        52: ['12', '8', '8', '11', '1'],
    }

    for tmp_item in center_top:
        if pieces[tmp_item] == 'W':
            do_seq(pos[tmp_item])
            break
