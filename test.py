'''Rubik's solver functions'''

from cube import pieces, default_pieces
from si import do_move

def test_solution():
    '''Find solution'''

    tmp_mids = [[1, 16],  [3, 41],  [5, 48],  [7, 28],  [10, 25], [12, 37],
                [14, 46], [19, 34], [21, 39], [23, 50], [30, 43], [32, 52]]

    tmp_pieces = [['W', 'R'], ['R', 'W'], ['W', 'O'], ['O', 'W'],
                  ['W', 'B'], ['B', 'W'], ['W', 'G'], ['G', 'W']]

    for mid in tmp_mids:
        for t_piece in tmp_pieces:
            tmp_test = False
            reset_test()
            pieces[mid[0]] = t_piece[0]
            pieces[mid[1]] = t_piece[1]
            if 'R' in t_piece:
                find_1(mid)
                if pieces[3] == 'W' and pieces[41] == 'R':
                    tmp_test = True
            elif 'O' in t_piece:
                find_2(mid)
                if pieces[5] == 'W' and pieces[48] == 'O':
                    tmp_test = True
            elif 'B' in t_piece:
                find_3(mid)
                if pieces[7] == 'W' and pieces[28] == 'B':
                    tmp_test = True
            elif 'G' in t_piece:
                find_4(mid)
                if pieces[1] == 'W' and pieces[16] == 'G':
                    tmp_test = True
            if tmp_test:
                print('[' + str(mid[0]) + ', ' + str(mid[1]) +
                      '] ' + t_piece[0] + ',' + t_piece[1] + ' passed')
            else:
                print('[' + str(mid[0]) + ', ' + str(mid[1]) +
                      '] ' + t_piece[0] + ',' + t_piece[1] + ' failed')
        print('')


def reset_test():
    for i, piece in enumerate(pieces):
        pieces[i] = 'B'


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
