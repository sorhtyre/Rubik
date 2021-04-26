'''User interface functions'''

import sys

from os import system as cli
from platform import system as arch
from random import randint
from random import choice

from cube import side_1, side_2, side_3, side_4, side_5, side_6
from cube import edge_1, edge_2, edge_3, edge_4, edge_5, edge_6
from cube import center_1, center_2, center_3
from log import write_log_item, delete_log_item, read_log, reset_log
from slog import reset_log as reset_slog
from move import rotate_cw, rotate_ccw, reset_cube
from solve_1 import find_solution
from test import test_solution

if arch() == 'Linux':
    CLEAR = 'clear'
else:
    CLEAR = 'cls'


def do_move(tmp_var):
    '''Execute move'''

    if tmp_var == '1':
        rotate_cw(side_2)
        rotate_cw(edge_2)
        write_log_item('[ 1] Side 2 - CW\r')
    elif tmp_var == '2':
        rotate_ccw(side_2)
        rotate_ccw(edge_2)
        write_log_item('[ 2] Side 2 - CCW\r')
    elif tmp_var == '3':
        rotate_ccw(side_4)
        rotate_ccw(edge_4)
        write_log_item('[ 3] Side 4 - CCW\r')
    elif tmp_var == '4':
        rotate_cw(side_4)
        rotate_cw(edge_4)
        write_log_item('[ 4] Side 4 - CW\r')
    elif tmp_var == '5':
        rotate_ccw(side_5)
        rotate_ccw(edge_5)
        write_log_item('[ 5] Side 5 - CCW\r')
    elif tmp_var == '6':
        rotate_cw(side_5)
        rotate_cw(edge_5)
        write_log_item('[ 6] Side 5 - CW\r')
    elif tmp_var == '7':
        rotate_cw(side_6)
        rotate_cw(edge_6)
        write_log_item('[ 7] Side 6 - CW\r')
    elif tmp_var == '8':
        rotate_ccw(side_6)
        rotate_ccw(edge_6)
        write_log_item('[ 8] Side 6 - CCW\r')
    elif tmp_var == '9':
        rotate_cw(side_3)
        rotate_cw(edge_3)
        write_log_item('[ 9] Side 3 - CW\r')
    elif tmp_var == '10':
        rotate_ccw(side_3)
        rotate_ccw(edge_3)
        write_log_item('[10] Side 3 - CCW\r')
    elif tmp_var == '11':
        rotate_ccw(side_1)
        rotate_ccw(edge_1)
        write_log_item('[11] Side 1 - CCW\r')
    elif tmp_var == '12':
        rotate_cw(side_1)
        rotate_cw(edge_1)
        write_log_item('[12] Side 1 - CW\r')
    elif tmp_var == 'SL':
        rotate_cw(side_2)
        rotate_cw(edge_2)
        rotate_ccw(center_1)
        rotate_ccw(side_4)
        rotate_ccw(edge_4)
        write_log_item('[SL] Shift cube left\r')
    if tmp_var == 'SR':
        rotate_ccw(side_2)
        rotate_ccw(edge_2)
        rotate_cw(center_1)
        rotate_cw(side_4)
        rotate_cw(edge_4)
        write_log_item('[SR] Shift cube right\r')
    elif tmp_var == 'SU':
        rotate_ccw(side_5)
        rotate_ccw(edge_5)
        rotate_ccw(center_2)
        rotate_cw(side_6)
        rotate_cw(edge_6)
        write_log_item('[SU] Shift cube up\r')
    elif tmp_var == 'SD':
        rotate_cw(side_5)
        rotate_cw(edge_5)
        rotate_cw(center_2)
        rotate_ccw(side_6)
        rotate_ccw(edge_6)
        write_log_item('[SR] Shift cube down\r')
    elif tmp_var == 'RL':
        rotate_cw(side_3)
        rotate_cw(edge_3)
        rotate_ccw(center_3)
        rotate_ccw(side_1)
        rotate_ccw(edge_1)
        write_log_item('[RL] Rotate cube left\r')
    elif tmp_var == 'RR':
        rotate_ccw(side_3)
        rotate_ccw(edge_3)
        rotate_cw(center_3)
        rotate_cw(side_1)
        rotate_cw(edge_1)
        write_log_item('[RR] Rotate cube right\r')
    elif tmp_var == 'T':
        works = True
        count = 0
        while works:
            reset_log()
            reset_slog()
            mix_cube()
            works = find_solution()
            count = count + 1
            print(count)
    elif tmp_var == 'F':
        reset_slog()
        find_solution()
    elif tmp_var == 'M':
        mix_cube()
    elif tmp_var == 'R':
        reset_cube()
        reset_log()
    elif tmp_var == 'U':
        undo_move()
    elif tmp_var == 'S':
        cli(CLEAR)
        print('Saving moves and quiting...')
        sys.exit()
    elif tmp_var == 'Q':
        cli(CLEAR)
        reset_log()
        print('Clearing moves and quiting...')
        sys.exit()


def undo_move():
    '''Undo last move'''

    line_list = read_log()

    if len(line_list) > 0:

        last_move = line_list[-1][1:3].strip()

        if last_move.isalpha():
            if last_move == 'SL':
                do_move('SR')
            elif last_move == 'SR':
                do_move('SL')
            elif last_move == 'SU':
                do_move('SD')
            elif last_move == 'SD':
                do_move('SU')
            elif last_move == 'RR':
                do_move('RL')
            elif last_move == 'RL':
                do_move('RR')
        else:
            opp = ['2', '1', '4', '3', '6', '5',
                   '8', '7', '10', '9', '12', '11']
            do_move(opp[int(last_move)-1])

        delete_log_item()


def load_move():
    '''Load moves from log'''

    line_list = read_log()

    if len(line_list) > 0:
        for tmp_line in line_list:
            do_move(tmp_line[1:3].strip())

        reset_log()

        for tmp_line in line_list:
            write_log_item(tmp_line)


def mix_cube():
    '''Randomly mix the cube'''

    tmp_int = randint(37, 42)
    for _ in range(tmp_int):
        tmp_choice = choice(['1', '2', '3', '4', '5', '6',
                             '7', '8', '9', '10', '11', '12'])
        do_move(tmp_choice)
