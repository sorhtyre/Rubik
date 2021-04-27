'''Rubik's solver functions'''

from cube import pieces
from si import do_move


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
        return True

    return False


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

    for tmp_item in center_left:

        if pieces[tmp_item] == 'W':

            if tmp_item == 1:
                do_move('11')

            elif tmp_item == 5:
                do_move('11')
                do_move('11')

            elif tmp_item == 7:
                do_move('12')

            elif tmp_item == 10:
                do_move('2')
                do_move('6')

            elif tmp_item == 12:
                do_move('6')

            elif tmp_item == 14:
                do_move('8')
                do_move('11')
                do_move('11')

            elif tmp_item == 16:
                do_move('1')
                do_move('6')

            elif tmp_item == 19:
                do_move('4')
                do_move('4')
                do_move('12')

            elif tmp_item == 21:
                do_move('6')
                do_move('6')

            elif tmp_item == 23:
                do_move('9')
                do_move('9')
                do_move('6')
                do_move('6')

            elif tmp_item == 25:
                do_move('2')
                do_move('2')
                do_move('11')

            elif tmp_item == 28:
                do_move('3')
                do_move('5')

            elif tmp_item == 30:
                do_move('5')

            elif tmp_item == 32:
                do_move('7')
                do_move('11')
                do_move('11')

            elif tmp_item == 34:
                do_move('4')
                do_move('5')

            elif tmp_item == 37:
                do_move('2')
                do_move('11')

            elif tmp_item == 39:
                do_move('5')
                do_move('4')
                do_move('12')

            elif tmp_item == 41:
                do_move('6')
                do_move('4')
                do_move('12')

            elif tmp_item == 43:
                do_move('4')
                do_move('12')

            elif tmp_item == 46:
                do_move('1')
                do_move('11')

            elif tmp_item == 48:
                do_move('7')
                do_move('1')
                do_move('11')

            elif tmp_item == 50:
                do_move('7')
                do_move('3')
                do_move('12')

            elif tmp_item == 52:
                do_move('3')
                do_move('12')

            break


def find_2(center_right):
    '''Find 2'''

    for tmp_item in center_right:

        if pieces[tmp_item] == 'W':

            if tmp_item == 1:
                do_move('2')
                do_move('2')
                do_move('10')
                do_move('8')
                do_move('8')

            elif tmp_item == 7:
                do_move('4')
                do_move('4')
                do_move('9')
                do_move('7')
                do_move('7')

            elif tmp_item == 10:
                do_move('1')
                do_move('8')

            elif tmp_item == 12:
                do_move('2')
                do_move('2')
                do_move('8')

            elif tmp_item == 14:
                do_move('8')

            elif tmp_item == 16:
                do_move('2')
                do_move('8')

            elif tmp_item == 19:
                do_move('9')
                do_move('8')
                do_move('8')

            elif tmp_item == 21:
                do_move('9')
                do_move('9')
                do_move('8')
                do_move('8')

            elif tmp_item == 23:
                do_move('8')
                do_move('8')

            elif tmp_item == 25:
                do_move('10')
                do_move('8')
                do_move('8')

            elif tmp_item == 28:
                do_move('4')
                do_move('7')

            elif tmp_item == 30:
                do_move('4')
                do_move('4')
                do_move('7')

            elif tmp_item == 32:
                do_move('7')

            elif tmp_item == 34:
                do_move('3')
                do_move('7')

            elif tmp_item == 37:
                do_move('1')
                do_move('10')
                do_move('8')
                do_move('8')

            elif tmp_item == 39:
                do_move('10')
                do_move('1')
                do_move('8')

            elif tmp_item == 43:
                do_move('3')
                do_move('9')
                do_move('8')
                do_move('8')

            elif tmp_item == 46:
                do_move('2')
                do_move('10')
                do_move('8')
                do_move('8')

            elif tmp_item == 48:
                do_move('8')
                do_move('4')
                do_move('9')
                do_move('8')
                do_move('8')

            elif tmp_item == 50:
                do_move('10')
                do_move('3')
                do_move('7')

            elif tmp_item == 52:
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
                do_move('2')
                do_move('2')
                do_move('10')
                do_move('10')
                do_move('4')
                do_move('4')

            elif tmp_item == 10:
                do_move('10')
                do_move('7')
                do_move('3')
                do_move('8')

            elif tmp_item == 12:
                do_move('1')
                do_move('10')
                do_move('7')
                do_move('3')
                do_move('8')

            elif tmp_item == 14:
                do_move('2')
                do_move('10')
                do_move('7')
                do_move('3')
                do_move('8')

            elif tmp_item == 16:
                do_move('2')
                do_move('2')
                do_move('10')
                do_move('7')
                do_move('3')
                do_move('8')
            elif tmp_item == 19:
                do_move('3')
                do_move('3')

            elif tmp_item == 21:
                do_move('9')
                do_move('3')
                do_move('3')

            elif tmp_item == 23:
                do_move('10')
                do_move('3')
                do_move('3')

            elif tmp_item == 25:
                do_move('9')
                do_move('9')
                do_move('3')
                do_move('3')

            elif tmp_item == 28:
                do_move('7')
                do_move('4')
                do_move('8')
                do_move('10')
                do_move('3')
                do_move('3')

            elif tmp_item == 30:
                do_move('7')
                do_move('4')
                do_move('4')
                do_move('8')
                do_move('10')
                do_move('3')
                do_move('3')

            elif tmp_item == 32:
                do_move('8')
                do_move('10')
                do_move('7')
                do_move('4')
                do_move('4')

            elif tmp_item == 34:
                do_move('8')
                do_move('9')
                do_move('7')
                do_move('3')

            elif tmp_item == 37:
                do_move('5')
                do_move('5')
                do_move('4')
                do_move('5')
                do_move('5')

            elif tmp_item == 39:
                do_move('5')
                do_move('4')
                do_move('6')

            elif tmp_item == 43:
                do_move('4')

            elif tmp_item == 46:
                do_move('7')
                do_move('7')
                do_move('3')
                do_move('8')
                do_move('8')

            elif tmp_item == 50:
                do_move('7')
                do_move('3')
                do_move('8')

            elif tmp_item == 52:
                do_move('3')

            break


def find_4(center_top):
    '''Find 4'''

    for tmp_item in center_top:

        if pieces[tmp_item] == 'W':

            if tmp_item == 10:
                do_move('10')
                do_move('8')
                do_move('1')
                do_move('7')

            elif tmp_item == 12:
                do_move('11')
                do_move('6')
                do_move('12')

            elif tmp_item == 14:
                do_move('12')
                do_move('8')
                do_move('11')

            elif tmp_item == 16:
                do_move('12')
                do_move('7')
                do_move('11')
                do_move('1')

            elif tmp_item == 19:
                do_move('10')
                do_move('10')
                do_move('1')
                do_move('1')

            elif tmp_item == 21:
                do_move('10')
                do_move('1')
                do_move('1')

            elif tmp_item == 23:
                do_move('9')
                do_move('2')
                do_move('2')

            elif tmp_item == 25:
                do_move('1')
                do_move('1')

            elif tmp_item == 30:
                do_move('11')
                do_move('5')
                do_move('12')

            elif tmp_item == 32:
                do_move('12')
                do_move('7')
                do_move('11')

            elif tmp_item == 34:
                do_move('7')
                do_move('9')
                do_move('8')
                do_move('1')

            elif tmp_item == 37:
                do_move('2')

            elif tmp_item == 39:
                do_move('11')
                do_move('6')
                do_move('12')
                do_move('2')

            elif tmp_item == 43:
                do_move('11')
                do_move('6')
                do_move('6')
                do_move('12')
                do_move('2')

            elif tmp_item == 46:
                do_move('1')

            elif tmp_item == 50:
                do_move('12')
                do_move('8')
                do_move('11')
                do_move('1')

            elif tmp_item == 52:
                do_move('12')
                do_move('8')
                do_move('8')
                do_move('11')
                do_move('1')

            break
