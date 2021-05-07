'''Solver interface functions'''

from common.switch import switch, args
from data.cube import u_moves, s_moves


def do_move(t_val):
    '''Execute move'''

    for i, func in enumerate(switch[t_val]):
        if func.__name__ == u_moves.append.__name__:
            func = s_moves.append
        if len(args[t_val]) > i:
            func(args[t_val][i])
        else:
            func()


def do_seq(arg_list):
    '''Do sequence of moves'''

    for arg in arg_list:
        do_move(arg)
