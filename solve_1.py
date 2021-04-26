'''Rubik's solver functions'''

from cube import pieces
from si import do_move

from solve_2 import find_solution as find_corners
from solve_3 import find_solution as find_edges
from solve_4 import find_solution as find_top
from solve_5 import find_solution as find_last
from debug import write_log_item

def find_solution():
    '''Find solution'''

    tmp_pieces = [['W', 'R'], ['W', 'O'], ['W', 'B'], ['W', 'G']]

    find_fcenter()
    find_ncenter()

    find_1(find_piece(tmp_pieces[0]))
    find_2(find_piece(tmp_pieces[1]))
    find_3(find_piece(tmp_pieces[2]))
    find_4(find_piece(tmp_pieces[3]))

    if pieces[1] == 'W' and pieces[16] == 'G' and \
       pieces[7] == 'W' and pieces[28] == 'B' and \
       pieces[5] == 'W' and pieces[48] == 'O' and \
       pieces[3] == 'W' and pieces[41] == 'R':
           if find_corners():
                if find_edges():
                    if find_top():
                        return(find_last())
           return(False)
    return(False)


def find_piece(t_piece):

    tmp_mids = [[1, 16],  [3, 41],  [5, 48],  [7, 28],  [10, 25], [12, 37],
                [14, 46], [19, 34], [21, 39], [23, 50], [30, 43], [32, 52]]

    for w_items in tmp_mids[:]:
        if t_piece[0] in [pieces[w_items[0]],
                          pieces[w_items[1]]]:
            if t_piece[1] in [pieces[w_items[0]],
                              pieces[w_items[1]]]:
                return(w_items)
                break


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

    for tmp_item in center_left:
        if pieces[tmp_item] == 'W':
            if tmp_item == 1:
                write_log_item('1 -1 - 1\r')
                do_move('11')
            elif tmp_item == 5:
                write_log_item('1 -1 - 5\r')
                do_move('11')
                do_move('11')
            elif tmp_item == 7:
                write_log_item('1 -1 - 7\r')
                do_move('12')
            elif tmp_item == 10:
                write_log_item('1 -1 - 10\r')
                do_move('2')
                do_move('6')
            elif tmp_item == 12:
                write_log_item('1 -1 - 12\r')
                do_move('6')
            elif tmp_item == 14:
                write_log_item('1 -1 - 14\r')
                do_move('8')
                do_move('11')
                do_move('11')
            elif tmp_item == 16:
                write_log_item('1 -1 - 16\r')
                do_move('1')
                do_move('6')
            elif tmp_item == 19:
                write_log_item('1 -1 - 19\r')
                do_move('4')
                do_move('4')
                do_move('12')
            elif tmp_item == 21:
                write_log_item('1 -1 - 21\r')
                do_move('6')
                do_move('6')
            elif tmp_item == 23:
                write_log_item('1 -1 - 23\r')
                do_move('9')
                do_move('9')
                do_move('6')
                do_move('6')
            elif tmp_item == 25:
                write_log_item('1 -1 - 25\r')
                do_move('2')
                do_move('2')
                do_move('11')
            elif tmp_item == 28:
                write_log_item('1 -1 - 28\r')
                do_move('3')
                do_move('5')
            elif tmp_item == 30:
                write_log_item('1 -1 - 30\r')
                do_move('5')
            elif tmp_item == 32:
                write_log_item('1 -1 - 32\r')
                do_move('7')
                do_move('11')
                do_move('11')
            elif tmp_item == 34:
                write_log_item('1 -1 - 34\r')
                do_move('4')
                do_move('5')
            elif tmp_item == 37:
                write_log_item('1 -1 - 37\r')
                do_move('2')
                do_move('11')
            elif tmp_item == 39:
                write_log_item('1 -1 - 39\r')
                do_move('5')
                do_move('4')
                do_move('12')
            elif tmp_item == 41:
                write_log_item('1 -1 - 41\r')
                do_move('6')
                do_move('4')
                do_move('12')
            elif tmp_item == 43:
                write_log_item('1 -1 - 43\r')
                do_move('4')
                do_move('12')
            elif tmp_item == 46:
                write_log_item('1 -1 - 46\r')
                do_move('1')
                do_move('11')
            elif tmp_item == 48:
                write_log_item('1 -1 - 48\r')
                do_move('7')
                do_move('1')
                do_move('11')
            elif tmp_item == 50:
                write_log_item('1 -1 - 50\r')
                do_move('7')
                do_move('3')
                do_move('12')
            elif tmp_item == 52:
                write_log_item('1 -1 - 52\r')
                do_move('3')
                do_move('12')
            break


def find_2(center_right):
    '''Find 2'''

    for tmp_item in center_right:
        if pieces[tmp_item] == 'W':
            if tmp_item == 1:
                write_log_item('1 -2 - 1\r')
                do_move('2')
                do_move('2')
                do_move('10')
                do_move('8')
                do_move('8')
            elif tmp_item == 7:
                write_log_item('1 -2 - 7\r')
                do_move('4')
                do_move('4')
                do_move('9')
                do_move('7')
                do_move('7')
            elif tmp_item == 10:
                write_log_item('1 -2 - 10\r')
                do_move('1')
                do_move('8')
            elif tmp_item == 12:
                write_log_item('1 -2 - 12\r')
                do_move('2')
                do_move('2')
                do_move('8')
            elif tmp_item == 14:
                write_log_item('1 -2 - 14\r')
                do_move('8')
            elif tmp_item == 16:
                write_log_item('1 -2 - 16\r')
                do_move('2')
                do_move('8')
            elif tmp_item == 19:
                write_log_item('1 -2 - 19\r')
                do_move('9')
                do_move('8')
                do_move('8')
            elif tmp_item == 21:
                write_log_item('1 -2 - 21\r')
                do_move('9')
                do_move('9')
                do_move('8')
                do_move('8')
            elif tmp_item == 23:
                write_log_item('1 -2 - 23\r')
                do_move('8')
                do_move('8')
            elif tmp_item == 25:
                write_log_item('1 -2 - 25\r')
                do_move('10')
                do_move('8')
                do_move('8')
            elif tmp_item == 28:
                write_log_item('1 -2 - 28\r')
                do_move('4')
                do_move('7')
            elif tmp_item == 30:
                write_log_item('1 -2 - 30\r')
                do_move('4')
                do_move('4')
                do_move('7')
            elif tmp_item == 32:
                write_log_item('1 -2 - 32\r')
                do_move('7')
            elif tmp_item == 34:
                write_log_item('1 -2 - 34\r')
                do_move('3')
                do_move('7')
            elif tmp_item == 37:
                write_log_item('1 -2 - 37\r')
                do_move('1')
                do_move('10')
                do_move('8')
                do_move('8')
            elif tmp_item == 39:
                write_log_item('1 -2 - 39\r')
                do_move('10')
                do_move('1')
                do_move('8')
            elif tmp_item == 43:
                write_log_item('1 -2 - 43\r')
                do_move('3')
                do_move('9')
                do_move('8')
                do_move('8')
            elif tmp_item == 46:
                write_log_item('1 -2 - 46\r')
                do_move('2')
                do_move('10')
                do_move('8')
                do_move('8')
            elif tmp_item == 48:
                write_log_item('1 -2 - 48\r')
                do_move('8')
                do_move('4')
                do_move('9')
                do_move('8')
                do_move('8')
            elif tmp_item == 50:
                write_log_item('1 -2 - 50\r')
                do_move('10')
                do_move('3')
                do_move('7')
            elif tmp_item == 52:
                write_log_item('1 -2 - 52\r')
                do_move('8')
                do_move('9')
                do_move('1')
                do_move('8')
            break


def find_3(center_bottom):
    '''Find 3'''

    for tmp_item in center_bottom:
        if pieces[tmp_item] == 'W':
            if tmp_item == 1:
                write_log_item('1 -3 - 1\r')
                do_move('2')
                do_move('2')
                do_move('10')
                do_move('10')
                do_move('4')
                do_move('4')
            elif tmp_item == 10:
                write_log_item('1 -3 - 10\r')
                do_move('10')
                do_move('7')
                do_move('3')
                do_move('8')
            elif tmp_item == 12:
                write_log_item('1 -3 - 12\r')
                do_move('1')
                do_move('10')
                do_move('7')
                do_move('3')
                do_move('8')
            elif tmp_item == 14:
                write_log_item('1 -3 - 14\r')
                do_move('2')
                do_move('10')
                do_move('7')
                do_move('3')
                do_move('8')
            elif tmp_item == 16:
                write_log_item('1 -3 - 16\r')
                do_move('2')
                do_move('2')
                do_move('10')
                do_move('7')
                do_move('3')
                do_move('8')
            elif tmp_item == 19:
                write_log_item('1 -3 - 19\r')
                do_move('3')
                do_move('3')
            elif tmp_item == 21:
                write_log_item('1 -3 - 21\r')
                do_move('9')
                do_move('3')
                do_move('3')
            elif tmp_item == 23:
                write_log_item('1 -3 - 23\r')
                do_move('10')
                do_move('3')
                do_move('3')
            elif tmp_item == 25:
                write_log_item('1 -3 - 25\r')
                do_move('9')
                do_move('9')
                do_move('3')
                do_move('3')
            elif tmp_item == 28:
                write_log_item('1 -3 - 28\r')
                do_move('7')
                do_move('4')
                do_move('8')
                do_move('10')
                do_move('3')
                do_move('3')
            elif tmp_item == 30:
                write_log_item('1 -3 - 30\r')
                do_move('7')
                do_move('4')
                do_move('4')
                do_move('8')
                do_move('10')
                do_move('3')
                do_move('3')
            elif tmp_item == 32:
                write_log_item('1 -3 - 32\r')
                do_move('8')
                do_move('10')
                do_move('7')
                do_move('4')
                do_move('4')
            elif tmp_item == 34:
                write_log_item('1 -3 - 34\r')
                do_move('8')
                do_move('9')
                do_move('7')
                do_move('3')
            elif tmp_item == 37:
                write_log_item('1 -3 - 37\r')
                do_move('5')
                do_move('5')
                do_move('4')
                do_move('5')
                do_move('5')
            elif tmp_item == 39:
                write_log_item('1 -3 - 39\r')
                do_move('5')
                do_move('4')
                do_move('6')
            elif tmp_item == 43:
                write_log_item('1 -3 - 43\r')
                do_move('4')
            elif tmp_item == 46:
                write_log_item('1 -3 - 46\r')
                do_move('7')
                do_move('7')
                do_move('3')
                do_move('8')
                do_move('8')
            elif tmp_item == 50:
                write_log_item('1 -3 - 50\r')
                do_move('7')
                do_move('3')
                do_move('8')
            elif tmp_item == 52:
                write_log_item('1 -3 - 52\r')
                do_move('3')
            break


def find_4(center_top):
    '''Find 4'''

    for tmp_item in center_top:
        if pieces[tmp_item] == 'W':
            if tmp_item == 10:
                write_log_item('1 -4 - 10\r')
                do_move('10')
                do_move('8')
                do_move('1')
                do_move('7')
            elif tmp_item == 12:
                write_log_item('1 -4 - 12\r')
                do_move('11')
                do_move('6')
                do_move('12')
            elif tmp_item == 14:
                write_log_item('1 -4 - 14\r')
                do_move('12')
                do_move('8')
                do_move('11')
            elif tmp_item == 16:
                write_log_item('1 -4 - 16\r')
                do_move('12')
                do_move('7')
                do_move('11')
                do_move('1')
            elif tmp_item == 19:
                write_log_item('1 -4 - 19\r')
                do_move('10')
                do_move('10')
                do_move('1')
                do_move('1')
            elif tmp_item == 21:
                write_log_item('1 -4 - 21\r')
                do_move('10')
                do_move('1')
                do_move('1')
            elif tmp_item == 23:
                write_log_item('1 -4 - 23\r')
                do_move('9')
                do_move('2')
                do_move('2')
            elif tmp_item == 25:
                write_log_item('1 -4 - 25\r')
                do_move('1')
                do_move('1')
            elif tmp_item == 30:
                write_log_item('1 -4 - 30\r')
                do_move('11')
                do_move('5')
                do_move('12')
            elif tmp_item == 32:
                write_log_item('1 -4 - 32\r')
                do_move('12')
                do_move('7')
                do_move('11')
            elif tmp_item == 34:
                write_log_item('1 -4 - 34\r')
                do_move('7')
                do_move('9')
                do_move('8')
                do_move('1')
            elif tmp_item == 37:
                write_log_item('1 -4 - 37\r')
                do_move('2')
            elif tmp_item == 39:
                write_log_item('1 -4 - 39\r')
                do_move('11')
                do_move('6')
                do_move('12')
                do_move('2')
            elif tmp_item == 43:
                write_log_item('1 -4 - 43\r')
                do_move('11')
                do_move('6')
                do_move('6')
                do_move('12')
                do_move('2')
            elif tmp_item == 46:
                write_log_item('1 -4 - 46\r')
                do_move('1')
            elif tmp_item == 50:
                write_log_item('1 -4 - 40\r')
                do_move('12')
                do_move('8')
                do_move('11')
                do_move('1')
            elif tmp_item == 52:
                write_log_item('1 -4 - 52\r')
                do_move('12')
                do_move('8')
                do_move('8')
                do_move('11')
                do_move('1')
            break
