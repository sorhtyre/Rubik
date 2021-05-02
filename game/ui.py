'''User interface functions'''

import time

from os import system as cli
from platform import system as arch
from random import randint
from random import choice

from common.log import read_log, write_log
from common.switch import switch, args
from data.cube import pieces, u_moves, s_moves
from solver.solve import solve_cube

from game.display import display
from game.move import reset_cube


if arch() == 'Linux':
    CLEAR = 'clear'
else:
    CLEAR = 'cls'


def do_move(t_val):
    '''Execute move'''

    if t_val == 'M':
        mix_cube()
    elif t_val == 'R':
        reset_cube()
        u_moves.clear()
    elif t_val == 'U':
        undo_move()
    elif t_val == 'F':
        find_solution()
    elif t_val == 'T':
        test_solver()
    else:
        try:
            for i, func in enumerate(switch[t_val]):
                if len(args[t_val]) > i:
                    func(args[t_val][i])
                else:
                    func()
        except KeyError:
            time.sleep(0)


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


def find_solution():
    '''Find solution for current cube'''

    t_cube = pieces[:]
    solve_cube()
    save_solution()
    pieces[:] = t_cube[:]


def save_solution():
    '''Save solution to file'''

    cli(CLEAR)
    write_log(['solve.log', s_moves])
    print('Saving solution to solve.log...')
    s_moves.clear()
    time.sleep(1)
    display()


def test_solver():
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
        print('\033[' + str(len("%i" % count)) + 'D', end='', flush=True)

    t_end = time.time()

    print('Solved ' + str(count) + ' random cubes in ' +
          str(t_end - t_start) + ' secs')
    print(str((t_end - t_start)/count) + ' secs per cube')
    time.sleep(5)
