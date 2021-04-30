'''User interface functions'''

import sys
import time

from os import system as cli
from platform import system as arch
from random import randint
from random import choice

from data.cube import pieces
from data.cube import side_1, side_2, side_3, side_4, side_5, side_6
from data.cube import edge_1, edge_2, edge_3, edge_4, edge_5, edge_6
from data.cube import center_1, center_2, center_3
from data.cube import u_moves, s_moves
from common.log import read_log, write_log
from solver.solve import solve_cube
# from tests.test import test_solution

from game.display import display
from game.move import rotate_cw, rotate_ccw, reset_cube

if arch() == 'Linux':
    CLEAR = 'clear'
else:
    CLEAR = 'cls'


def do_move(tmp_var):
    '''Execute move'''

    if tmp_var == '1':
        rotate_cw(side_2)
        rotate_cw(edge_2)
        u_moves.append('[ 1] Side 2 - CW\r')
    elif tmp_var == '2':
        rotate_ccw(side_2)
        rotate_ccw(edge_2)
        u_moves.append('[ 2] Side 2 - CCW\r')
    elif tmp_var == '3':
        rotate_ccw(side_4)
        rotate_ccw(edge_4)
        u_moves.append('[ 3] Side 4 - CCW\r')
    elif tmp_var == '4':
        rotate_cw(side_4)
        rotate_cw(edge_4)
        u_moves.append('[ 4] Side 4 - CW\r')
    elif tmp_var == '5':
        rotate_ccw(side_5)
        rotate_ccw(edge_5)
        u_moves.append('[ 5] Side 5 - CCW\r')
    elif tmp_var == '6':
        rotate_cw(side_5)
        rotate_cw(edge_5)
        u_moves.append('[ 6] Side 5 - CW\r')
    elif tmp_var == '7':
        rotate_cw(side_6)
        rotate_cw(edge_6)
        u_moves.append('[ 7] Side 6 - CW\r')
    elif tmp_var == '8':
        rotate_ccw(side_6)
        rotate_ccw(edge_6)
        u_moves.append('[ 8] Side 6 - CCW\r')
    elif tmp_var == '9':
        rotate_cw(side_3)
        rotate_cw(edge_3)
        u_moves.append('[ 9] Side 3 - CW\r')
    elif tmp_var == '10':
        rotate_ccw(side_3)
        rotate_ccw(edge_3)
        u_moves.append('[10] Side 3 - CCW\r')
    elif tmp_var == '11':
        rotate_ccw(side_1)
        rotate_ccw(edge_1)
        u_moves.append('[11] Side 1 - CCW\r')
    elif tmp_var == '12':
        rotate_cw(side_1)
        rotate_cw(edge_1)
        u_moves.append('[12] Side 1 - CW\r')
    elif tmp_var == 'SL':
        rotate_cw(side_2)
        rotate_cw(edge_2)
        rotate_ccw(center_1)
        rotate_ccw(side_4)
        rotate_ccw(edge_4)
        u_moves.append('[SL] Shift cube left\r')
    if tmp_var == 'SR':
        rotate_ccw(side_2)
        rotate_ccw(edge_2)
        rotate_cw(center_1)
        rotate_cw(side_4)
        rotate_cw(edge_4)
        u_moves.append('[SR] Shift cube right\r')
    elif tmp_var == 'SU':
        rotate_ccw(side_5)
        rotate_ccw(edge_5)
        rotate_ccw(center_2)
        rotate_cw(side_6)
        rotate_cw(edge_6)
        u_moves.append('[SU] Shift cube up\r')
    elif tmp_var == 'SD':
        rotate_cw(side_5)
        rotate_cw(edge_5)
        rotate_cw(center_2)
        rotate_ccw(side_6)
        rotate_ccw(edge_6)
        u_moves.append('[SR] Shift cube down\r')
    elif tmp_var == 'RL':
        rotate_cw(side_3)
        rotate_cw(edge_3)
        rotate_ccw(center_3)
        rotate_ccw(side_1)
        rotate_ccw(edge_1)
        u_moves.append('[RL] Rotate cube left\r')
    elif tmp_var == 'RR':
        rotate_ccw(side_3)
        rotate_ccw(edge_3)
        rotate_cw(center_3)
        rotate_cw(side_1)
        rotate_cw(edge_1)
        u_moves.append('[RR] Rotate cube right\r')
    elif tmp_var == 'T':
        test_cube()
    elif tmp_var == 'F':
        t_cube = pieces[:]
        solve_cube()
        save_solution()
        pieces[:] = t_cube[:]
    elif tmp_var == 'M':
        mix_cube()
    elif tmp_var == 'R':
        reset_cube()
        u_moves.clear()
    elif tmp_var == 'U':
        undo_move()
    elif tmp_var == 'S':
        cli(CLEAR)
        write_log('cube.log', u_moves)
        print('Saving moves...')
        time.sleep(.5)
        display()
    elif tmp_var == 'E':
        cli(CLEAR)
        write_log('cube.log', u_moves)
        print('Exiting and saving moves...')
        sys.exit()
    elif tmp_var == 'Q':
        cli(CLEAR)
        print('Quiting without saving...')
        sys.exit()


def undo_move():
    '''Undo last move'''

    if len(u_moves) > 0:

        tmp_move = u_moves.pop()
        last_move = tmp_move[1:3].strip()

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

        u_moves.pop()


def load_cube():
    '''Load cube moves from log'''

    tmp_lines = read_log('cube.log')

    if len(tmp_lines) > 0:
        for t_line in tmp_lines:
            do_move(t_line[1:3].strip())


def mix_cube():
    '''Randomly mix the cube'''

    tmp_int = randint(37, 42)
    for _ in range(tmp_int):
        tmp_choice = choice(['1', '2', '3', '4', '5', '6',
                             '7', '8', '9', '10', '11', '12'])
        do_move(tmp_choice)


def test_cube():
    '''Test random generated cubes'''

    t_start = time.time()

    works = True
    count = 0
    cli(CLEAR)

    print('Solving: ', end='', flush=True)

    while works and count < 10000:
        count = count + 1
        print(count, end='', flush=True)
        mix_cube()
        works = solve_cube()
        u_moves.clear()
        s_moves.clear()
        print('\033['+ str(len("%i" % count)) +'D', end='', flush=True)

    t_end = time.time()

    print('Solved ' + str(count) + ' random cubes in ' +
          str(t_end - t_start) + ' secs')
    print(str((t_end - t_start)/count) + ' secs per cube')
    time.sleep(5)


def save_solution():
    '''Save solution to file'''

    cli(CLEAR)
    write_log('solve.log', s_moves)
    print('Saving solution to solve.log...')
    s_moves.clear()
    time.sleep(1)
    display()
