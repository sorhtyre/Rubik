'''Rubik's solver functions'''

import sys

from cube import pieces
from si import do_move

from debug import write_log_item


def find_solution():
    '''Find solution'''

    while not find_mids():
        symbol()
        find_0()
        

    while [pieces[18], pieces[20], pieces[24], pieces[26]].count('Y') != 4:
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
            return(False)
        find_1()

    return(True)


def find_mids():
    '''Find mids'''

    if pieces[19] == 'Y' and pieces[21] == 'Y' and \
       pieces[23] == 'Y' and pieces[25] == 'Y':
        return(True)
    return(False)


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

    if pieces[18] == 'Y' and pieces[19] == 'Y' and pieces[21] == 'Y' and \
       pieces[23] == 'Y' and pieces[25] == 'Y':
       do_move('10')
    elif pieces[19] == 'Y' and pieces[20] == 'Y' and pieces[21] == 'Y' and \
         pieces[23] == 'Y' and pieces[25] == 'Y':
         do_move('10')
         do_move('10')
    elif pieces[19] == 'Y' and pieces[21] == 'Y' and pieces[23] == 'Y' and \
         pieces[25] == 'Y' and pieces[26] == 'Y':
         do_move('9')

def find_b():
    '''Plus'''

    if pieces[9] == 'Y' and pieces[11] == 'Y':
       do_move(9)
    elif pieces[45] == 'Y' and pieces[47] == 'Y':
         do_move(9)
         do_move(9)
    elif pieces[33] == 'Y' and pieces[29] == 'Y':
         do_move(10)


def find_c():
    '''School'''

    if pieces[19] == 'Y' and pieces[21] == 'Y' and pieces[23] == 'Y' and \
       pieces[24] == 'Y' and pieces[25] == 'Y' and pieces[26] == 'Y':
           do_move('10')
    elif pieces[18] == 'Y' and pieces[19] == 'Y' and pieces[21] == 'Y' and \
         pieces[23] == 'Y' and pieces[24] == 'Y' and pieces[25] == 'Y':
             do_move('10')
             do_move('10')
    elif pieces[18] == 'Y' and pieces[19] == 'Y' and pieces[20] == 'Y' and \
         pieces[21] == 'Y' and pieces[23] == 'Y' and pieces[25] == 'Y':
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

    write_log_item('4 -1 - 0\r')
    do_move('1')
    do_move('9')
    do_move('7')
    do_move('10')
    do_move('8')
    do_move('2')

def find_1():
    '''Find 1'''

    write_log_item('4 -1 - 1\r')
    do_move('7')
    do_move('9')
    do_move('8')
    do_move('9')
    do_move('7')
    do_move('9')
    do_move('9')
    do_move('8')
