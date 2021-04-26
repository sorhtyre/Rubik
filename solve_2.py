'''Rubik's solver functions'''

from cube import pieces
from si import do_move


def find_solution():
    '''Find solution'''

    tmp_pieces = [['W', 'R', 'G'], ['W', 'B', 'R'],
                  ['W', 'G', 'O'], ['W', 'O', 'B']]

    find_5(find_piece(tmp_pieces[0]))
    find_6(find_piece(tmp_pieces[1]))
    find_7(find_piece(tmp_pieces[2]))
    find_8(find_piece(tmp_pieces[3]))

    return(pieces[8] == 'W' and pieces[51] == 'O' and pieces[29] == 'B' and
           pieces[2] == 'W' and pieces[45] == 'O' and pieces[17] == 'G' and
           pieces[6] == 'W' and pieces[44] == 'R' and pieces[27] == 'B' and
           pieces[0] == 'W' and pieces[38] == 'R' and pieces[15] == 'G')


def find_piece(t_piece):
    '''Find piece'''

    tmp_corners = [[0, 38, 15],  [2, 17, 45],  [6, 27, 44],  [8, 51, 29],
                   [18, 42, 33], [20, 35, 53], [24, 9, 36],  [26, 47, 11]]

    for w_items in tmp_corners[:]:
        if t_piece[0] in [pieces[w_items[0]],
                          pieces[w_items[1]],
                          pieces[w_items[2]]]:
            if t_piece[1] in [pieces[w_items[0]],
                              pieces[w_items[1]],
                              pieces[w_items[2]]]:
                if t_piece[2] in [pieces[w_items[0]],
                                  pieces[w_items[1]],
                                  pieces[w_items[2]]]:
                    return w_items
    return None


def find_5(top_left):
    '''Find 1'''

    for tmp_item in top_left:

        if pieces[tmp_item] == 'W':

            if tmp_item == 2:
                do_move('7')
                do_move('10')
                do_move('8')
                do_move('5')
                do_move('9')
                do_move('6')

            elif tmp_item == 6:
                do_move('3')
                do_move('9')
                do_move('4')
                do_move('1')
                do_move('10')
                do_move('2')

            elif tmp_item == 8:
                do_move('8')
                do_move('10')
                do_move('7')
                do_move('10')
                do_move('1')
                do_move('9')
                do_move('2')

            elif tmp_item == 9:
                do_move('1')
                do_move('9')
                do_move('2')

            elif tmp_item == 11:
                do_move('10')
                do_move('1')
                do_move('9')
                do_move('9')
                do_move('2')

            elif tmp_item == 15:
                do_move('1')
                do_move('9')
                do_move('2')
                do_move('10')
                do_move('1')
                do_move('9')
                do_move('2')

            elif tmp_item == 17:
                do_move('7')
                do_move('10')
                do_move('8')
                do_move('9')
                do_move('5')
                do_move('10')
                do_move('6')

            elif tmp_item == 18:
                do_move('7')
                do_move('9')
                do_move('8')
                do_move('9')
                do_move('5')
                do_move('10')
                do_move('6')

            elif tmp_item == 20:
                do_move('9')
                do_move('7')
                do_move('5')
                do_move('9')
                do_move('9')
                do_move('6')
                do_move('8')

            elif tmp_item == 24:
                do_move('10')
                do_move('7')
                do_move('5')
                do_move('9')
                do_move('9')
                do_move('6')
                do_move('8')

            elif tmp_item == 26:
                do_move('7')
                do_move('5')
                do_move('9')
                do_move('9')
                do_move('6')
                do_move('8')

            elif tmp_item == 27:
                do_move('3')
                do_move('10')
                do_move('4')
                do_move('2')
                do_move('6')
                do_move('1')
                do_move('5')

            elif tmp_item == 29:
                do_move('4')
                do_move('9')
                do_move('3')
                do_move('5')
                do_move('9')
                do_move('6')

            elif tmp_item == 33:
                do_move('1')
                do_move('10')
                do_move('2')

            elif tmp_item == 35:
                do_move('5')
                do_move('9')
                do_move('9')
                do_move('6')

            elif tmp_item == 36:
                do_move('9')
                do_move('1')
                do_move('10')
                do_move('2')

            elif tmp_item == 38:
                do_move('5')
                do_move('10')
                do_move('6')
                do_move('9')
                do_move('5')
                do_move('10')
                do_move('6')

            elif tmp_item == 42:
                do_move('10')
                do_move('1')
                do_move('9')
                do_move('2')

            elif tmp_item == 44:
                do_move('3')
                do_move('9')
                do_move('4')
                do_move('10')
                do_move('1')
                do_move('9')
                do_move('2')

            elif tmp_item == 45:
                do_move('7')
                do_move('5')
                do_move('9')
                do_move('6')
                do_move('8')

            elif tmp_item == 47:
                do_move('5')
                do_move('9')
                do_move('6')

            elif tmp_item == 51:
                do_move('8')
                do_move('10')
                do_move('7')
                do_move('1')
                do_move('10')
                do_move('2')

            elif tmp_item == 53:
                do_move('1')
                do_move('9')
                do_move('9')
                do_move('2')

            break


def find_6(bot_left):
    '''Find 2'''

    for tmp_item in bot_left:

        if pieces[tmp_item] == 'W':

            if tmp_item == 2:
                do_move('6')
                do_move('7')
                do_move('10')
                do_move('10')
                do_move('5')
                do_move('8')

            elif tmp_item == 8:
                do_move('8')
                do_move('9')
                do_move('7')
                do_move('6')
                do_move('10')
                do_move('5')

            elif tmp_item == 9:
                do_move('9')
                do_move('6')
                do_move('9')
                do_move('5')

            elif tmp_item == 11:
                do_move('6')
                do_move('9')
                do_move('9')
                do_move('5')

            elif tmp_item == 17:
                do_move('2')
                do_move('6')
                do_move('9')
                do_move('9')
                do_move('5')
                do_move('1')

            elif tmp_item == 18:
                do_move('3')
                do_move('9')
                do_move('4')
                do_move('6')
                do_move('9')
                do_move('9')
                do_move('5')

            elif tmp_item == 20:
                do_move('4')
                do_move('5')
                do_move('3')
                do_move('6')
                do_move('3')
                do_move('9')
                do_move('4')

            elif tmp_item == 24:
                do_move('5')
                do_move('4')
                do_move('6')
                do_move('3')
                do_move('6')
                do_move('10')
                do_move('5')

            elif tmp_item == 26:
                do_move('6')
                do_move('9')
                do_move('5')
                do_move('9')
                do_move('6')
                do_move('10')
                do_move('5')

            elif tmp_item == 27:
                do_move('6')
                do_move('10')
                do_move('5')
                do_move('9')
                do_move('6')
                do_move('10')
                do_move('5')

            elif tmp_item == 29:
                do_move('8')
                do_move('9')
                do_move('7')
                do_move('10')
                do_move('6')
                do_move('9')
                do_move('5')

            elif tmp_item == 33:
                do_move('9')
                do_move('6')
                do_move('10')
                do_move('5')

            elif tmp_item == 35:
                do_move('10')
                do_move('6')
                do_move('9')
                do_move('5')

            elif tmp_item == 36:
                do_move('10')
                do_move('6')
                do_move('9')
                do_move('9')
                do_move('5')

            elif tmp_item == 42:
                do_move('4')
                do_move('5')
                do_move('3')
                do_move('6')

            elif tmp_item == 44:
                do_move('3')
                do_move('9')
                do_move('4')
                do_move('4')
                do_move('5')
                do_move('3')
                do_move('6')

            elif tmp_item == 45:
                do_move('7')
                do_move('3')
                do_move('9')
                do_move('9')
                do_move('4')
                do_move('8')

            elif tmp_item == 47:
                do_move('7')
                do_move('6')
                do_move('10')
                do_move('5')
                do_move('8')

            elif tmp_item == 51:
                do_move('6')
                do_move('8')
                do_move('10')
                do_move('5')
                do_move('7')

            elif tmp_item == 53:
                do_move('6')
                do_move('10')
                do_move('5')

            break


def find_7(top_right):
    '''Find 3'''

    for tmp_item in top_right:

        if pieces[tmp_item] == 'W':

            if tmp_item == 8:
                do_move('4')
                do_move('10')
                do_move('3')
                do_move('2')
                do_move('9')
                do_move('1')

            elif tmp_item == 9:
                do_move('10')
                do_move('7')
                do_move('9')
                do_move('8')

            elif tmp_item == 11:
                do_move('9')
                do_move('7')
                do_move('10')
                do_move('8')

            elif tmp_item == 17:
                do_move('7')
                do_move('10')
                do_move('8')
                do_move('2')
                do_move('10')
                do_move('1')

            elif tmp_item == 18:
                do_move('2')
                do_move('10')
                do_move('1')
                do_move('7')
                do_move('9')
                do_move('8')

            elif tmp_item == 20:
                do_move('10')
                do_move('2')
                do_move('10')
                do_move('1')
                do_move('7')
                do_move('9')
                do_move('8')

            elif tmp_item == 24:
                do_move('7')
                do_move('10')
                do_move('10')
                do_move('8')
                do_move('2')
                do_move('10')
                do_move('1')

            elif tmp_item == 26:
                do_move('2')
                do_move('10')
                do_move('10')
                do_move('1')
                do_move('9')
                do_move('2')
                do_move('10')
                do_move('1')

            elif tmp_item == 29:
                do_move('4')
                do_move('2')
                do_move('9')
                do_move('1')
                do_move('3')

            elif tmp_item == 33:
                do_move('9')
                do_move('9')
                do_move('2')
                do_move('10')
                do_move('1')

            elif tmp_item == 35:
                do_move('2')
                do_move('9')
                do_move('1')

            elif tmp_item == 36:
                do_move('10')
                do_move('2')
                do_move('10')
                do_move('1')

            elif tmp_item == 42:
                do_move('2')
                do_move('10')
                do_move('10')
                do_move('1')

            elif tmp_item == 45:
                do_move('2')
                do_move('9')
                do_move('1')
                do_move('7')
                do_move('9')
                do_move('8')

            elif tmp_item == 47:
                do_move('10')
                do_move('2')
                do_move('9')
                do_move('1')

            elif tmp_item == 51:
                do_move('4')
                do_move('10')
                do_move('3')
                do_move('9')
                do_move('2')
                do_move('10')
                do_move('1')

            elif tmp_item == 53:
                do_move('9')
                do_move('2')
                do_move('10')
                do_move('1')

            break


def find_8(bot_right):
    '''Find 4'''

    for tmp_item in bot_right:

        if pieces[tmp_item] == 'W':

            if tmp_item == 9:
                do_move('8')
                do_move('10')
                do_move('10')
                do_move('7')

            elif tmp_item == 11:
                do_move('10')
                do_move('8')
                do_move('10')
                do_move('7')

            elif tmp_item == 18:
                do_move('3')
                do_move('7')
                do_move('4')
                do_move('8')
                do_move('10')
                do_move('8')
                do_move('10')
                do_move('7')

            elif tmp_item == 20:
                do_move('8')
                do_move('10')
                do_move('10')
                do_move('7')
                do_move('9')
                do_move('8')
                do_move('10')
                do_move('7')

            elif tmp_item == 24:
                do_move('8')
                do_move('10')
                do_move('7')
                do_move('10')
                do_move('8')
                do_move('9')
                do_move('7')

            elif tmp_item == 26:
                do_move('9')
                do_move('8')
                do_move('10')
                do_move('7')
                do_move('4')
                do_move('9')
                do_move('3')

            elif tmp_item == 29:
                do_move('8')
                do_move('9')
                do_move('7')
                do_move('4')
                do_move('9')
                do_move('3')

            elif tmp_item == 33:
                do_move('9')
                do_move('9')
                do_move('4')
                do_move('10')
                do_move('3')

            elif tmp_item == 35:
                do_move('4')
                do_move('9')
                do_move('3')

            elif tmp_item == 36:
                do_move('4')
                do_move('10')
                do_move('10')
                do_move('3')

            elif tmp_item == 42:
                do_move('8')
                do_move('9')
                do_move('7')

            elif tmp_item == 47:
                do_move('10')
                do_move('4')
                do_move('9')
                do_move('3')

            elif tmp_item == 51:
                do_move('4')
                do_move('10')
                do_move('3')
                do_move('8')
                do_move('10')
                do_move('7')

            elif tmp_item == 53:
                do_move('9')
                do_move('4')
                do_move('10')
                do_move('3')

            break
