'''Rubik's solver functions'''

from data.cube import pieces
from solver.si import do_move


def find_solution():
    '''Find solution'''

    tmp_pieces = [['R', 'G'], ['G', 'O'], ['O', 'B'], ['B', 'R']]

    find_1(find_piece(tmp_pieces[0]))
    find_2(find_piece(tmp_pieces[1]))
    find_3(find_piece(tmp_pieces[2]))
    find_4(find_piece(tmp_pieces[3]))

    return(pieces[12] == 'G' and pieces[37] == 'R' and
           pieces[14] == 'G' and pieces[46] == 'O' and
           pieces[30] == 'B' and pieces[43] == 'R' and
           pieces[32] == 'B' and pieces[52] == 'O')


def find_piece(t_piece):
    '''Find piece'''

    tmp_mids = [[12, 37], [10, 25], [14, 46], [50, 23],
                [32, 52], [34, 19], [30, 43], [39, 21]]

    for w_items in tmp_mids[:]:
        if t_piece[0] in [pieces[w_items[0]], pieces[w_items[1]]]:
            if t_piece[1] in [pieces[w_items[0]], pieces[w_items[1]]]:
                return w_items
    return None


def find_1(center_left):
    '''Find 1'''

    for tmp_item in center_left:

        if pieces[tmp_item] == 'R':

            if tmp_item == 10:
                do_move('9')
                do_move('9')
                do_move('1')
                do_move('10')
                do_move('2')
                do_move('10')
                do_move('5')
                do_move('9')
                do_move('6')

            elif tmp_item == 12:
                do_move('1')
                do_move('10')
                do_move('2')
                do_move('10')
                do_move('5')
                do_move('9')
                do_move('6')
                do_move('10')
                do_move('1')
                do_move('10')
                do_move('2')
                do_move('10')
                do_move('5')
                do_move('9')
                do_move('6')

            elif tmp_item == 14:
                do_move('7')
                do_move('10')
                do_move('8')
                do_move('10')
                do_move('2')
                do_move('9')
                do_move('1')
                do_move('9')
                do_move('5')
                do_move('9')
                do_move('6')
                do_move('9')
                do_move('1')
                do_move('10')
                do_move('2')

            elif tmp_item == 19:
                do_move('9')
                do_move('5')
                do_move('9')
                do_move('6')
                do_move('9')
                do_move('1')
                do_move('10')
                do_move('2')

            elif tmp_item == 21:
                do_move('10')
                do_move('10')
                do_move('5')
                do_move('9')
                do_move('6')
                do_move('9')
                do_move('1')
                do_move('10')
                do_move('2')

            elif tmp_item == 23:
                do_move('5')
                do_move('9')
                do_move('6')
                do_move('9')
                do_move('1')
                do_move('10')
                do_move('2')

            elif tmp_item == 25:
                do_move('10')
                do_move('5')
                do_move('9')
                do_move('6')
                do_move('9')
                do_move('1')
                do_move('10')
                do_move('2')

            elif tmp_item == 30:
                do_move('6')
                do_move('10')
                do_move('5')
                do_move('10')
                do_move('3')
                do_move('9')
                do_move('4')
                do_move('10')
                do_move('5')
                do_move('9')
                do_move('6')
                do_move('9')
                do_move('1')
                do_move('10')
                do_move('2')

            elif tmp_item == 32:
                do_move('8')
                do_move('9')
                do_move('7')
                do_move('9')
                do_move('4')
                do_move('10')
                do_move('3')
                do_move('10')
                do_move('5')
                do_move('9')
                do_move('6')
                do_move('9')
                do_move('1')
                do_move('10')
                do_move('2')

            elif tmp_item == 34:
                do_move('1')
                do_move('10')
                do_move('2')
                do_move('10')
                do_move('5')
                do_move('9')
                do_move('6')

            elif tmp_item == 39:
                do_move('9')
                do_move('1')
                do_move('10')
                do_move('2')
                do_move('10')
                do_move('5')
                do_move('9')
                do_move('6')

            elif tmp_item == 43:
                do_move('3')
                do_move('9')
                do_move('4')
                do_move('9')
                do_move('6')
                do_move('10')
                do_move('5')
                do_move('5')
                do_move('9')
                do_move('6')
                do_move('9')
                do_move('1')
                do_move('10')
                do_move('2')

            elif tmp_item == 46:
                do_move('2')
                do_move('9')
                do_move('1')
                do_move('9')
                do_move('7')
                do_move('10')
                do_move('8')
                do_move('10')
                do_move('10')
                do_move('5')
                do_move('9')
                do_move('6')
                do_move('9')
                do_move('1')
                do_move('10')
                do_move('2')

            elif tmp_item == 50:
                do_move('10')
                do_move('1')
                do_move('10')
                do_move('2')
                do_move('10')
                do_move('5')
                do_move('9')
                do_move('6')

            elif tmp_item == 52:
                do_move('4')
                do_move('10')
                do_move('3')
                do_move('10')
                do_move('8')
                do_move('9')
                do_move('7')
                do_move('10')
                do_move('10')
                do_move('5')
                do_move('9')
                do_move('6')
                do_move('9')
                do_move('1')
                do_move('10')
                do_move('2')

            break


def find_2(center_right):
    '''Find 2'''

    for tmp_item in center_right:

        if pieces[tmp_item] == 'G':

            if tmp_item == 10:
                do_move('9')
                do_move('7')
                do_move('10')
                do_move('8')
                do_move('10')
                do_move('2')
                do_move('9')
                do_move('1')

            elif tmp_item == 19:
                do_move('2')
                do_move('9')
                do_move('1')
                do_move('9')
                do_move('7')
                do_move('10')
                do_move('8')

            elif tmp_item == 21:
                do_move('9')
                do_move('2')
                do_move('9')
                do_move('1')
                do_move('9')
                do_move('7')
                do_move('10')
                do_move('8')

            elif tmp_item == 23:
                do_move('10')
                do_move('2')
                do_move('9')
                do_move('1')
                do_move('9')
                do_move('7')
                do_move('10')
                do_move('8')

            elif tmp_item == 25:
                do_move('9')
                do_move('9')
                do_move('2')
                do_move('9')
                do_move('1')
                do_move('9')
                do_move('7')
                do_move('10')
                do_move('8')

            elif tmp_item == 30:
                do_move('6')
                do_move('10')
                do_move('5')
                do_move('10')
                do_move('3')
                do_move('9')
                do_move('4')
                do_move('9')
                do_move('9')
                do_move('2')
                do_move('9')
                do_move('1')
                do_move('9')
                do_move('7')
                do_move('10')
                do_move('8')

            elif tmp_item == 32:
                do_move('8')
                do_move('9')
                do_move('7')
                do_move('9')
                do_move('4')
                do_move('10')
                do_move('3')
                do_move('9')
                do_move('9')
                do_move('2')
                do_move('9')
                do_move('1')
                do_move('9')
                do_move('7')
                do_move('10')
                do_move('8')

            elif tmp_item == 34:
                do_move('10')
                do_move('7')
                do_move('10')
                do_move('8')
                do_move('10')
                do_move('2')
                do_move('9')
                do_move('1')

            elif tmp_item == 39:
                do_move('7')
                do_move('10')
                do_move('8')
                do_move('10')
                do_move('2')
                do_move('9')
                do_move('1')

            elif tmp_item == 43:
                do_move('6')
                do_move('10')
                do_move('5')
                do_move('10')
                do_move('3')
                do_move('9')
                do_move('4')
                do_move('9')
                do_move('7')
                do_move('10')
                do_move('8')
                do_move('10')
                do_move('2')
                do_move('9')
                do_move('1')

            elif tmp_item == 46:
                do_move('7')
                do_move('10')
                do_move('8')
                do_move('10')
                do_move('2')
                do_move('9')
                do_move('1')
                do_move('10')
                do_move('7')
                do_move('10')
                do_move('8')
                do_move('10')
                do_move('2')
                do_move('9')
                do_move('1')

            elif tmp_item == 50:
                do_move('9')
                do_move('9')
                do_move('7')
                do_move('10')
                do_move('8')
                do_move('10')
                do_move('2')
                do_move('9')
                do_move('1')

            elif tmp_item == 52:
                do_move('8')
                do_move('9')
                do_move('7')
                do_move('9')
                do_move('4')
                do_move('10')
                do_move('3')
                do_move('9')
                do_move('7')
                do_move('10')
                do_move('8')
                do_move('10')
                do_move('2')
                do_move('9')
                do_move('1')

            break


def find_3(center_bottom):
    '''Find 3'''

    for tmp_item in center_bottom:

        if pieces[tmp_item] == 'O':

            if tmp_item == 10:
                do_move('4')
                do_move('10')
                do_move('3')
                do_move('10')
                do_move('8')
                do_move('9')
                do_move('7')

            elif tmp_item == 19:
                do_move('10')
                do_move('8')
                do_move('9')
                do_move('7')
                do_move('9')
                do_move('4')
                do_move('10')
                do_move('3')

            elif tmp_item == 21:
                do_move('8')
                do_move('9')
                do_move('7')
                do_move('9')
                do_move('4')
                do_move('10')
                do_move('3')

            elif tmp_item == 23:
                do_move('9')
                do_move('9')
                do_move('8')
                do_move('9')
                do_move('7')
                do_move('9')
                do_move('4')
                do_move('10')
                do_move('3')

            elif tmp_item == 25:
                do_move('9')
                do_move('8')
                do_move('9')
                do_move('7')
                do_move('9')
                do_move('4')
                do_move('10')
                do_move('3')

            elif tmp_item == 30:
                do_move('6')
                do_move('10')
                do_move('5')
                do_move('10')
                do_move('3')
                do_move('9')
                do_move('4')
                do_move('9')
                do_move('8')
                do_move('9')
                do_move('7')
                do_move('9')
                do_move('4')
                do_move('10')
                do_move('3')

            elif tmp_item == 32:
                do_move('8')
                do_move('9')
                do_move('7')
                do_move('9')
                do_move('4')
                do_move('10')
                do_move('3')
                do_move('9')
                do_move('8')
                do_move('9')
                do_move('7')
                do_move('9')
                do_move('4')
                do_move('10')
                do_move('3')

            elif tmp_item == 34:
                do_move('9')
                do_move('9')
                do_move('4')
                do_move('10')
                do_move('3')
                do_move('10')
                do_move('8')
                do_move('9')
                do_move('7')

            elif tmp_item == 39:
                do_move('10')
                do_move('4')
                do_move('10')
                do_move('3')
                do_move('10')
                do_move('8')
                do_move('9')
                do_move('7')

            elif tmp_item == 43:
                do_move('6')
                do_move('10')
                do_move('5')
                do_move('10')
                do_move('3')
                do_move('9')
                do_move('4')
                do_move('4')
                do_move('10')
                do_move('3')
                do_move('10')
                do_move('8')
                do_move('9')
                do_move('7')

            elif tmp_item == 50:
                do_move('9')
                do_move('4')
                do_move('10')
                do_move('3')
                do_move('10')
                do_move('8')
                do_move('9')
                do_move('7')

            break


def find_4(center_top):
    '''Find 4'''

    for tmp_item in center_top:

        if pieces[tmp_item] == 'B':

            if tmp_item == 10:
                do_move('10')
                do_move('6')
                do_move('10')
                do_move('5')
                do_move('10')
                do_move('3')
                do_move('9')
                do_move('4')

            elif tmp_item == 19:
                do_move('9')
                do_move('9')
                do_move('3')
                do_move('9')
                do_move('4')
                do_move('9')
                do_move('6')
                do_move('10')
                do_move('5')

            elif tmp_item == 21:
                do_move('10')
                do_move('3')
                do_move('9')
                do_move('4')
                do_move('9')
                do_move('6')
                do_move('10')
                do_move('5')

            elif tmp_item == 23:
                do_move('9')
                do_move('3')
                do_move('9')
                do_move('4')
                do_move('9')
                do_move('6')
                do_move('10')
                do_move('5')

            elif tmp_item == 25:
                do_move('3')
                do_move('9')
                do_move('4')
                do_move('9')
                do_move('6')
                do_move('10')
                do_move('5')

            elif tmp_item == 34:
                do_move('9')
                do_move('6')
                do_move('10')
                do_move('5')
                do_move('10')
                do_move('3')
                do_move('9')
                do_move('4')

            elif tmp_item == 39:
                do_move('9')
                do_move('9')
                do_move('6')
                do_move('10')
                do_move('5')
                do_move('10')
                do_move('3')
                do_move('9')
                do_move('4')

            elif tmp_item == 43:
                do_move('6')
                do_move('10')
                do_move('5')
                do_move('10')
                do_move('3')
                do_move('9')
                do_move('4')
                do_move('10')
                do_move('6')
                do_move('10')
                do_move('5')
                do_move('10')
                do_move('3')
                do_move('9')
                do_move('4')

            elif tmp_item == 50:
                do_move('6')
                do_move('10')
                do_move('5')
                do_move('10')
                do_move('3')
                do_move('9')
                do_move('4')

            break
