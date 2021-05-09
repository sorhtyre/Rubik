'''User interface functions'''

import time
import multiprocessing

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

    switch.update({'M':  [mix_cube],
                   'R':  [reset_cube, u_moves.clear],
                   'U':  [undo_move],
                   'F':  [find_solution],
                   'T':  [test_solver],
                   'TM': [test_mult_solver]})

    args.update({'M': [], 'R': [], 'U': [], 'F': [], 'T': [], 'TM': []})

    if t_val == '':
        time.sleep(0)
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

    t_start = time.process_time()

    works = True
    count = 0
    len_moves = []
    cli(CLEAR)

    print('Solving: ', end='', flush=True)

    while works and count < 10000:
        count += 1
        print(count, end='', flush=True)
        mix_cube()
        works = solve_cube()
        len_moves.append(len(s_moves))
        u_moves.clear()
        s_moves.clear()
        print('\033[' + str(len("%i" % count)) + 'D', end='', flush=True)

    cli(CLEAR)
    t_end = time.process_time()

    print('Solved ' + str(count) + ' random cubes in ' +
          str(t_end - t_start) + ' secs')
    print(str((t_end - t_start)/count) + ' secs per cube')

    min_moves = min(len_moves)
    max_moves = max(len_moves)
    avg_moves = sum(len_moves) / count

    print('Min moves to solve: ' + str(min_moves))
    print('Max moves to solve: ' + str(max_moves))
    print('Avg moves to solve: ' + str(avg_moves))

    time.sleep(10)


def test_mult_solver():
    '''Test random generated cubes'''

    t_start = time.perf_counter()

    count = 10000
    cli(CLEAR)

    with multiprocessing.Pool() as pool:
        ret_moves = pool.map(solver_call, range(count))

    t_end = time.perf_counter()

    print('Solved ' + str(count) + ' random cubes in ' +
          str(t_end - t_start) + ' secs')
    print(str((t_end - t_start)/count) + ' secs per cube')

    min_moves = min(ret_moves)
    max_moves = max(ret_moves)
    avg_moves = sum(ret_moves) / count

    print('Min moves to solve: ' + str(min_moves))
    print('Max moves to solve: ' + str(max_moves))
    print('Avg moves to solve: ' + str(avg_moves))

    time.sleep(10)


def solver_call(count):
    '''Solver call'''

    print('Solving' + '.' * int((10 / 10000) * count), end='\r', flush=True)
    mix_cube()
    solve_cube()
    len_moves = len(s_moves)
    u_moves.clear()
    s_moves.clear()

    return len_moves
