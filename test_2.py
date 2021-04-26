'''Rubik's solver functions'''

from cube import pieces, default_pieces
from si import do_move

def test_solution():
    '''Find solution'''

    tmp_corners = [[0, 38, 15],  [2, 17, 45],  [6, 27, 44],  [8, 51, 29],
                  [18, 42, 33], [20, 35, 53], [24, 9, 36], [26, 47, 11]]

    for corner in tmp_corners:
        reset_test()
#        pieces[corner[0]] = 'W'
#        pieces[corner[1]] = 'R'
#        pieces[corner[2]] = 'G'
#        find_1(corner)
#        pieces[corner[0]] = 'W'
#        pieces[corner[1]] = 'B'
#        pieces[corner[2]] = 'R'
#        find_2(corner)
#        pieces[corner[0]] = 'W'
#        pieces[corner[1]] = 'G'
#        pieces[corner[2]] = 'O'
#        find_3(corner)
        pieces[corner[0]] = 'W'
        pieces[corner[1]] = 'O'
        pieces[corner[2]] = 'B'
        find_4(corner)
        if pieces[8] == 'W' and pieces[51] == 'O' and pieces[29] == 'B' and \
           pieces[2] == 'W' and pieces[45] == 'O' and pieces[17] == 'G' and \
           pieces[6] == 'W' and pieces[44] == 'R' and pieces[27] == 'B' and \
           pieces[0] == 'W' and pieces[38] == 'R' and pieces[15] == 'G' and \
           pieces[1] == 'W' and pieces[16] == 'G' and \
           pieces[7] == 'W' and pieces[28] == 'B' and \
           pieces[5] == 'W' and pieces[48] == 'O' and \
           pieces[3] == 'W' and pieces[41] == 'R':
            print('[' + str(corner[0]) + ', ' + str(corner[1]) +', ' + str(corner[2]) +
                  '] W,O,B passed')
        else:
            print('[' + str(corner[0]) + ', ' + str(corner[1]) +', ' + str(corner[2]) +
                  '] W,O,B failed')
        reset_test()
#        pieces[corner[0]] = 'R'
#        pieces[corner[1]] = 'G'
#        pieces[corner[2]] = 'W'
#        find_1(corner)
#        pieces[corner[0]] = 'B'
#        pieces[corner[1]] = 'R'
#        pieces[corner[2]] = 'W'
#        find_2(corner)
#        pieces[corner[0]] = 'G'
#        pieces[corner[1]] = 'O'
#        pieces[corner[2]] = 'W'
#        find_3(corner)
        pieces[corner[0]] = 'O'
        pieces[corner[1]] = 'B'
        pieces[corner[2]] = 'W'
        find_4(corner)
        if pieces[8] == 'W' and pieces[51] == 'O' and pieces[29] == 'B' and \
           pieces[2] == 'W' and pieces[45] == 'O' and pieces[17] == 'G' and \
           pieces[6] == 'W' and pieces[44] == 'R' and pieces[27] == 'B' and \
           pieces[0] == 'W' and pieces[38] == 'R' and pieces[15] == 'G' and \
           pieces[1] == 'W' and pieces[16] == 'G' and \
           pieces[7] == 'W' and pieces[28] == 'B' and \
           pieces[5] == 'W' and pieces[48] == 'O' and \
           pieces[3] == 'W' and pieces[41] == 'R':
            print('[' + str(corner[0]) + ', ' + str(corner[1]) +', ' + str(corner[2]) +
                  '] O,B,W passed')
        else:
            print('[' + str(corner[0]) + ', ' + str(corner[1]) +', ' + str(corner[2]) +
                  '] O,B,W failed')
        reset_test()
#        pieces[corner[0]] = 'G'
#        pieces[corner[1]] = 'W'
#        pieces[corner[2]] = 'R'
#        find_1(corner)
#        pieces[corner[0]] = 'R'
#        pieces[corner[1]] = 'W'
#        pieces[corner[2]] = 'B'
#        find_2(corner)
#        pieces[corner[0]] = 'O'
#        pieces[corner[1]] = 'W'
#        pieces[corner[2]] = 'G'
#        find_3(corner)
        pieces[corner[0]] = 'B'
        pieces[corner[1]] = 'W'
        pieces[corner[2]] = 'O'
        find_4(corner)
        if pieces[8] == 'W' and pieces[51] == 'O' and pieces[29] == 'B' and \
           pieces[2] == 'W' and pieces[45] == 'O' and pieces[17] == 'G' and \
           pieces[6] == 'W' and pieces[44] == 'R' and pieces[27] == 'B' and \
           pieces[0] == 'W' and pieces[38] == 'R' and pieces[15] == 'G' and \
           pieces[1] == 'W' and pieces[16] == 'G' and \
           pieces[7] == 'W' and pieces[28] == 'B' and \
           pieces[5] == 'W' and pieces[48] == 'O' and \
           pieces[3] == 'W' and pieces[41] == 'R':
            print('[' + str(corner[0]) + ', ' + str(corner[1]) +', ' + str(corner[2]) +
                  '] B,W,O passed')
        else:
            print('[' + str(corner[0]) + ', ' + str(corner[1]) +', ' + str(corner[2]) +
                  '] B,W,O failed')
    print('')


def reset_test():
    for i, piece in enumerate(pieces):
        pieces[i] = 'B'

    pieces[3] = 'W'
    pieces[41] = 'R'

    pieces[5] = 'W'
    pieces[48] = 'O'

    pieces[7] = 'W'
    pieces[28] = 'B'

    pieces[1] = 'W'
    pieces[16] = 'G'

    pieces[0] = 'W'
    pieces[38] = 'R'
    pieces[15] = 'G'

    pieces[6] = 'W'
    pieces[27] = 'B'
    pieces[44] = 'R'

    pieces[2] = 'W'
    pieces[17] = 'G'
    pieces[45] = 'O'


def find_piece(t_piece):

    tmp_corners = [[0, 38, 15],  [2, 17, 45],  [6, 44, 27],  [8, 29, 51],
                  [18, 33, 42], [20, 35, 53], [24, 9, 36], [26, 47, 11]]

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


def find_1(top_left):
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


def find_2(bot_left):
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


def find_3(top_right):
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


def find_4(bot_right):
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
