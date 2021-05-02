'''Rubik's solver functions'''

from data.cube import pieces
from solver.si import do_move


def find_solution():
    '''Find solution'''

    while not pieces[19] == pieces[21] == pieces[23] == pieces[25] == 'Y':
        symbol()
        find_0()

    while not pieces[18] == pieces[20] == pieces[24] == pieces[26] == 'Y':
        tmp_count = [pieces[18], pieces[20], pieces[24], pieces[26]].count('Y')

        if tmp_count == 0:
            find_b()
        elif tmp_count == 1:
            find_a()
        elif tmp_count == 2:
            if (pieces[18] == 'Y' and pieces[26] == 'Y') or \
               (pieces[20] == 'Y' and pieces[24] == 'Y'):
                find_d()
            else:
                find_c()
        elif tmp_count == 3:
            return False

        find_1()

    return True


def symbol():
    '''Symbols'''

    if pieces[19] == 'Y' and pieces[23] == 'Y':
        do_move('10')
    elif pieces[23] == 'Y' and pieces[25] == 'Y':
        do_move('10')
        do_move('10')
    elif pieces[25] == 'Y' and pieces[21] == 'Y':
        do_move('9')
    elif pieces[19] == 'Y' and pieces[25] == 'Y':
        do_move('10')


def find_a():
    '''Fish'''

    if pieces[18] == pieces[19] == pieces[21] == pieces[23] == pieces[25] == 'Y':
        do_move('10')
    elif pieces[19] == pieces[20] == pieces[21] == pieces[23] == pieces[25] == 'Y':
        do_move('10')
        do_move('10')
    elif pieces[19] == pieces[21] == pieces[23] == pieces[25] == pieces[26] == 'Y':
        do_move('9')


def find_b():
    '''Plus'''

    if pieces[9] == 'Y' and pieces[11] == 'Y':
        do_move('9')
    elif pieces[45] == 'Y' and pieces[47] == 'Y':
        do_move('9')
        do_move('9')
    elif pieces[33] == 'Y' and pieces[29] == 'Y':
        do_move('10')


def find_c():
    '''School'''

    if pieces[19] == pieces[21] == pieces[23] == pieces[24] == pieces[25] == pieces[26] == 'Y':
        do_move('10')
    elif pieces[18] == pieces[19] == pieces[21] == pieces[23] == pieces[24] == pieces[25] == 'Y':
        do_move('10')
        do_move('10')
    elif pieces[18] == pieces[19] == pieces[20] == pieces[21] == pieces[23] == pieces[25] == 'Y':
        do_move('9')


def find_d():
    '''Diamonds'''

    if pieces[45] == 'Y':
        do_move('9')
    elif pieces[33] == 'Y':
        do_move('9')
        do_move('9')
    elif pieces[36] == 'Y':
        do_move('10')


def find_0():
    '''Find 0'''

    do_move('1')
    do_move('9')
    do_move('7')
    do_move('10')
    do_move('8')
    do_move('2')


def find_1():
    '''Find 1'''

    do_move('7')
    do_move('9')
    do_move('8')
    do_move('9')
    do_move('7')
    do_move('9')
    do_move('9')
    do_move('8')
