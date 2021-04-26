'''Rubik's solver functions'''

from cube import pieces
from si import do_move

from debug import write_log_item


def find_solution():
    '''Find solution'''

    tmp_pieces = [['W', 'R', 'G'], ['W', 'B', 'R'],
                  ['W', 'G', 'O'], ['W', 'O', 'B']]

    find_5(find_piece(tmp_pieces[0]))
    find_6(find_piece(tmp_pieces[1]))
    find_7(find_piece(tmp_pieces[2]))
    find_8(find_piece(tmp_pieces[3]))

    return(pieces[8] == 'W' and pieces[51] == 'O' and pieces[29] == 'B' and \
           pieces[2] == 'W' and pieces[45] == 'O' and pieces[17] == 'G' and \
           pieces[6] == 'W' and pieces[44] == 'R' and pieces[27] == 'B' and \
           pieces[0] == 'W' and pieces[38] == 'R' and pieces[15] == 'G')


def find_piece(t_piece):

    tmp_corners = [[0, 38, 15],  [2, 17, 45],  [6, 27, 44],  [8, 51, 29],
                  [18, 42, 33], [20, 35, 53], [24, 9, 36], [26, 47, 11]]

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
                    return(w_items)
                    break


def find_5(top_left):
    '''Find 1'''

    for tmp_item in top_left:
        if pieces[tmp_item] == 'W':
            if tmp_item == 2:
                write_log_item('2 -1 - 2\r')
                do_move('7')
                do_move('10')
                do_move('8')
                do_move('5')
                do_move('9')
                do_move('6')
            elif tmp_item == 6:
                write_log_item('2 -1 - 6\r')
                do_move('3')
                do_move('9')
                do_move('4')
                do_move('1')
                do_move('10')
                do_move('2')
            elif tmp_item == 8:
                write_log_item('2 -1 - 8\r')
                do_move('8')
                do_move('10')
                do_move('7')
                do_move('10')
                do_move('1')
                do_move('9')
                do_move('2')
            elif tmp_item == 9:
                write_log_item('2 -1 - 9\r')
                do_move('1')
                do_move('9')
                do_move('2')
            elif tmp_item == 11:
                write_log_item('2 -1 - 11\r')
                do_move('10')
                do_move('1')
                do_move('9')
                do_move('9')
                do_move('2')
            elif tmp_item == 15:
                write_log_item('2 -1 - 15\r')
                do_move('1')
                do_move('9')
                do_move('2')
                do_move('10')
                do_move('1')
                do_move('9')
                do_move('2')
            elif tmp_item == 17:
                write_log_item('2 -1 - 17\r')
                do_move('7')
                do_move('10')
                do_move('8')
                do_move('9')
                do_move('5')
                do_move('10')
                do_move('6')
            elif tmp_item == 18:
                write_log_item('2 -1 - 18\r')
                do_move('7')
                do_move('9')
                do_move('8')
                do_move('9')
                do_move('5')
                do_move('10')
                do_move('6')
            elif tmp_item == 20:
                write_log_item('2 -1 - 20\r')
                do_move('9')
                do_move('7')
                do_move('5')
                do_move('9')
                do_move('9')
                do_move('6')
                do_move('8')
            elif tmp_item == 24:
                write_log_item('2 -1 - 24\r')
                do_move('10')
                do_move('7')
                do_move('5')
                do_move('9')
                do_move('9')
                do_move('6')
                do_move('8')
            elif tmp_item == 26:
                write_log_item('2 -1 - 26\r')
                do_move('7')
                do_move('5')
                do_move('9')
                do_move('9')
                do_move('6')
                do_move('8')
            elif tmp_item == 27:
                write_log_item('2 -1 - 27\r')
                do_move('3')
                do_move('10')
                do_move('4')
                do_move('2')
                do_move('6')
                do_move('1')
                do_move('5')
            elif tmp_item == 29:
                write_log_item('2 -1 - 29\r')
                do_move('4')
                do_move('9')
                do_move('3')
                do_move('5')
                do_move('9')
                do_move('6')
            elif tmp_item == 33:
                write_log_item('2 -1 - 33\r')
                do_move('1')
                do_move('10')
                do_move('2')
            elif tmp_item == 35:
                write_log_item('2 -1 - 35\r')
                do_move('5')
                do_move('9')
                do_move('9')
                do_move('6')
            elif tmp_item == 36:
                write_log_item('2 -1 - 36\r')
                do_move('9')
                do_move('1')
                do_move('10')
                do_move('2')
            elif tmp_item == 38:
                write_log_item('2 -1 - 38\r')
                do_move('5')
                do_move('10')
                do_move('6')
                do_move('9')
                do_move('5')
                do_move('10')
                do_move('6')
            elif tmp_item == 42:
                write_log_item('2 -1 - 42\r')
                do_move('10')
                do_move('1')
                do_move('9')
                do_move('2')
            elif tmp_item == 44:
                write_log_item('2 -1 - 44\r')
                do_move('3')
                do_move('9')
                do_move('4')
                do_move('10')
                do_move('1')
                do_move('9')
                do_move('2')
            elif tmp_item == 45:
                write_log_item('2 -1 - 45\r')
                do_move('7')
                do_move('5')
                do_move('9')
                do_move('6')
                do_move('8')
            elif tmp_item == 47:
                write_log_item('2 -1 - 47\r')
                do_move('5')
                do_move('9')
                do_move('6')
            elif tmp_item == 51:
                write_log_item('2 -1 - 51\r')
                do_move('8')
                do_move('10')
                do_move('7')
                do_move('1')
                do_move('10')
                do_move('2')
            elif tmp_item == 53:
                write_log_item('2 -1 - 53\r')
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
                write_log_item('2 -2 - 2\r')
                do_move('6')
                do_move('7')
                do_move('10')
                do_move('10')
                do_move('5')
                do_move('8')
            elif tmp_item == 8:
                write_log_item('2 -2 - 8\r')
                do_move('8')
                do_move('9')
                do_move('7')
                do_move('6')
                do_move('10')
                do_move('5')
            elif tmp_item == 9:
                write_log_item('2 -2 - 9\r')
                do_move('9')
                do_move('6')
                do_move('9')
                do_move('5')
            elif tmp_item == 11:
                write_log_item('2 -2 - 11\r')
                do_move('6')
                do_move('9')
                do_move('9')
                do_move('5')
            elif tmp_item == 17:
                write_log_item('2 -2 - 17\r')
                do_move('2')
                do_move('6')
                do_move('9')
                do_move('9')
                do_move('5')
                do_move('1')
            elif tmp_item == 18:
                write_log_item('2 -2 - 18\r')
                do_move('3')
                do_move('9')
                do_move('4')
                do_move('6')
                do_move('9')
                do_move('9')
                do_move('5')
            elif tmp_item == 20:
                write_log_item('2 -2 - 20\r')
                do_move('4')
                do_move('5')
                do_move('3')
                do_move('6')
                do_move('3')
                do_move('9')
                do_move('4')
            elif tmp_item == 24:
                write_log_item('2 -2 - 24\r')
                do_move('5')
                do_move('4')
                do_move('6')
                do_move('3')
                do_move('6')
                do_move('10')
                do_move('5')
            elif tmp_item == 26:
                write_log_item('2 -2 - 26\r')
                do_move('6')
                do_move('9')
                do_move('5')
                do_move('9')
                do_move('6')
                do_move('10')
                do_move('5')
            elif tmp_item == 27:
                write_log_item('2 -2 - 27\r')
                do_move('6')
                do_move('10')
                do_move('5')
                do_move('9')
                do_move('6')
                do_move('10')
                do_move('5')
            elif tmp_item == 29:
                write_log_item('2 -2 - 29\r')
                do_move('8')
                do_move('9')
                do_move('7')
                do_move('10')
                do_move('6')
                do_move('9')
                do_move('5')
            elif tmp_item == 33:
                write_log_item('2 -2 - 33\r')
                do_move('9')
                do_move('6')
                do_move('10')
                do_move('5')
            elif tmp_item == 35:
                write_log_item('2 -2 - 35\r')
                do_move('10')
                do_move('6')
                do_move('9')
                do_move('5')
            elif tmp_item == 36:
                write_log_item('2 -2 - 36\r')
                do_move('10')
                do_move('6')
                do_move('9')
                do_move('9')
                do_move('5')
            elif tmp_item == 42:
                write_log_item('2 -2 - 42\r')
                do_move('4')
                do_move('5')
                do_move('3')
                do_move('6')
            elif tmp_item == 44:
                write_log_item('2 -2 - 44\r')
                do_move('3')
                do_move('9')
                do_move('4')
                do_move('4')
                do_move('5')
                do_move('3')
                do_move('6')
            elif tmp_item == 45:
                write_log_item('2 -2 - 45\r')
                do_move('7')
                do_move('3')
                do_move('9')
                do_move('9')
                do_move('4')
                do_move('8')
            elif tmp_item == 47:
                write_log_item('2 -2 - 47\r')
                do_move('7')
                do_move('6')
                do_move('10')
                do_move('5')
                do_move('8')
            elif tmp_item == 51:
                write_log_item('2 -2 - 51\r')
                do_move('6')
                do_move('8')
                do_move('10')
                do_move('5')
                do_move('7')
            elif tmp_item == 53:
                write_log_item('2 -2 - 53\r')
                do_move('6')
                do_move('10')
                do_move('5')
            break


def find_7(top_right):
    '''Find 3'''

    for tmp_item in top_right:
        if pieces[tmp_item] == 'W':
            if tmp_item == 8:
                write_log_item('2 -3 - 8\r')
                do_move('4')
                do_move('10')
                do_move('3')
                do_move('2')
                do_move('9')
                do_move('1')
            elif tmp_item == 9:
                write_log_item('2 -3 - 9\r')
                do_move('10')
                do_move('7')
                do_move('9')
                do_move('8')
            elif tmp_item == 11:
                write_log_item('2 -3 - 11\r')
                do_move('9')
                do_move('7')
                do_move('10')
                do_move('8')
            elif tmp_item == 17:
                write_log_item('2 -3 - 17\r')
                do_move('7')
                do_move('10')
                do_move('8')
                do_move('2')
                do_move('10')
                do_move('1')
            elif tmp_item == 18:
                write_log_item('2 -3 - 18\r')
                do_move('2')
                do_move('10')
                do_move('1')
                do_move('7')
                do_move('9')
                do_move('8')
            elif tmp_item == 20:
                write_log_item('2 -3 - 20\r')
                do_move('10')
                do_move('2')
                do_move('10')
                do_move('1')
                do_move('7')
                do_move('9')
                do_move('8')
            elif tmp_item == 24:
                write_log_item('2 -3 - 24\r')
                do_move('7')
                do_move('10')
                do_move('10')
                do_move('8')
                do_move('2')
                do_move('10')
                do_move('1')
            elif tmp_item == 26:
                write_log_item('2 -3 - 26\r')
                do_move('2')
                do_move('10')
                do_move('10')
                do_move('1')
                do_move('9')
                do_move('2')
                do_move('10')
                do_move('1')
            elif tmp_item == 29:
                write_log_item('2 -3 - 29\r')
                do_move('4')
                do_move('2')
                do_move('9')
                do_move('1')
                do_move('3')
            elif tmp_item == 33:
                write_log_item('2 -3 - 33\r')
                do_move('9')
                do_move('9')
                do_move('2')
                do_move('10')
                do_move('1')
            elif tmp_item == 35:
                write_log_item('2 -3 - 35\r')
                do_move('2')
                do_move('9')
                do_move('1')
            elif tmp_item == 36:
                write_log_item('2 -3 - 36\r')
                do_move('10')
                do_move('2')
                do_move('10')
                do_move('1')
            elif tmp_item == 42:
                write_log_item('2 -3 - 42\r')
                do_move('2')
                do_move('10')
                do_move('10')
                do_move('1')
            elif tmp_item == 45:
                write_log_item('2 -3 - 45\r')
                do_move('2')
                do_move('9')
                do_move('1')
                do_move('7')
                do_move('9')
                do_move('8')
            elif tmp_item == 47:
                write_log_item('2 -3 - 47\r')
                do_move('10')
                do_move('2')
                do_move('9')
                do_move('1')
            elif tmp_item == 51:
                write_log_item('2 -3 - 51\r')
                do_move('4')
                do_move('10')
                do_move('3')
                do_move('9')
                do_move('2')
                do_move('10')
                do_move('1')
            elif tmp_item == 53:
                write_log_item('2 -3 - 53\r')
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
                write_log_item('2 -4 - 9\r')
                do_move('8')
                do_move('10')
                do_move('10')
                do_move('7')
            elif tmp_item == 11:
                write_log_item('2 -4 - 11\r')
                do_move('10')
                do_move('8')
                do_move('10')
                do_move('7')
            elif tmp_item == 18:
                write_log_item('2 -4 - 18\r')
                do_move('3')
                do_move('7')
                do_move('4')
                do_move('8')
                do_move('10')
                do_move('8')
                do_move('10')
                do_move('7')
            elif tmp_item == 20:
                write_log_item('2 -4 - 20\r')
                do_move('8')
                do_move('10')
                do_move('10')
                do_move('7')
                do_move('9')
                do_move('8')
                do_move('10')
                do_move('7')
            elif tmp_item == 24:
                write_log_item('2 -4 - 24\r')
                do_move('8')
                do_move('10')
                do_move('7')
                do_move('10')
                do_move('8')
                do_move('9')
                do_move('7')
            elif tmp_item == 26:
                write_log_item('2 -4 - 26\r')
                do_move('9')
                do_move('8')
                do_move('10')
                do_move('7')
                do_move('4')
                do_move('9')
                do_move('3')
            elif tmp_item == 29:
                write_log_item('2 -4 - 29\r')
                do_move('8')
                do_move('9')
                do_move('7')
                do_move('4')
                do_move('9')
                do_move('3')
            elif tmp_item == 33:
                write_log_item('2 -4 - 33\r')
                do_move('9')
                do_move('9')
                do_move('4')
                do_move('10')
                do_move('3')
            elif tmp_item == 35:
                write_log_item('2 -4 - 35\r')
                do_move('4')
                do_move('9')
                do_move('3')
            elif tmp_item == 36:
                write_log_item('2 -4 - 36\r')
                do_move('4')
                do_move('10')
                do_move('10')
                do_move('3')
            elif tmp_item == 42:
                write_log_item('2 -4 - 42\r')
                do_move('8')
                do_move('9')
                do_move('7')
            elif tmp_item == 47:
                write_log_item('2 -4 - 47\r')
                do_move('10')
                do_move('4')
                do_move('9')
                do_move('3')
            elif tmp_item == 51:
                write_log_item('2 -4 - 51\r')
                do_move('4')
                do_move('10')
                do_move('3')
                do_move('8')
                do_move('10')
                do_move('7')
            elif tmp_item == 53:
                write_log_item('2 -4 - 53\r')
                do_move('9')
                do_move('4')
                do_move('10')
                do_move('3')
            break
