'''Input switch'''

import sys
import time

from os import system as cli
from platform import system as arch

from data.cube import side_1, side_2, side_3, side_4, side_5, side_6
from data.cube import edge_1, edge_2, edge_3, edge_4, edge_5, edge_6
from data.cube import center_1, center_2, center_3
from data.cube import u_moves
from game.display import display
from game.move import rotate_cw, rotate_ccw

from common.log import write_log

if arch() == 'Linux':
    CLEAR = 'clear'
else:
    CLEAR = 'cls'

switch = {
    '1':  [rotate_cw, rotate_cw, u_moves.append],
    '2':  [rotate_ccw, rotate_ccw, u_moves.append],
    '3':  [rotate_ccw, rotate_ccw, u_moves.append],
    '4':  [rotate_cw, rotate_cw, u_moves.append],
    '5':  [rotate_ccw, rotate_ccw, u_moves.append],
    '6':  [rotate_cw, rotate_cw, u_moves.append],
    '7':  [rotate_cw, rotate_cw, u_moves.append],
    '8':  [rotate_ccw, rotate_ccw, u_moves.append],
    '9':  [rotate_cw, rotate_cw, u_moves.append],
    '10': [rotate_ccw, rotate_ccw, u_moves.append],
    '11': [rotate_ccw, rotate_ccw, u_moves.append],
    '12': [rotate_cw, rotate_cw, u_moves.append],
    'SL': [rotate_cw, rotate_cw, rotate_ccw, rotate_ccw, rotate_ccw, u_moves.append],
    'SR': [rotate_ccw, rotate_ccw, rotate_cw, rotate_cw, rotate_cw, u_moves.append],
    'SU': [rotate_ccw, rotate_ccw, rotate_ccw, rotate_cw, rotate_cw, u_moves.append],
    'SD': [rotate_cw, rotate_cw, rotate_cw, rotate_ccw, rotate_ccw, u_moves.append],
    'RL': [rotate_cw, rotate_cw, rotate_ccw, rotate_ccw, rotate_ccw, u_moves.append],
    'RR': [rotate_ccw, rotate_ccw, rotate_cw, rotate_cw, rotate_cw, u_moves.append],
    'S':  [cli, write_log, print, time.sleep, display],
    'E':  [cli, write_log, print, sys.exit],
    'Q':  [cli, print, sys.exit]
}

args = {
    '1':  [side_2, edge_2, '[ 1] Side 2 - CW\r'],
    '2':  [side_2, edge_2, '[ 2] Side 2 - CCW\r'],
    '3':  [side_4, edge_4, '[ 3] Side 4 - CCW\r'],
    '4':  [side_4, edge_4, '[ 4] Side 4 - CW\r'],
    '5':  [side_5, edge_5, '[ 5] Side 5 - CCW\r'],
    '6':  [side_5, edge_5, '[ 6] Side 5 - CW\r'],
    '7':  [side_6, edge_6, '[ 7] Side 6 - CW\r'],
    '8':  [side_6, edge_6, '[ 8] Side 6 - CCW\r'],
    '9':  [side_3, edge_3, '[ 9] Side 3 - CW\r'],
    '10': [side_3, edge_3, '[10] Side 3 - CCW\r'],
    '11': [side_1, edge_1, '[11] Side 1 - CCW\r'],
    '12': [side_1, edge_1, '[12] Side 1 - CW\r'],
    'SL': [side_2, edge_2, center_1, side_4, edge_4, '[SL] Shift cube left\r'],
    'SR': [side_2, edge_2, center_1, side_4, edge_4, '[SR] Shift cube right\r'],
    'SU': [side_5, edge_5, center_2, side_6, edge_6, '[SU] Shift cube up\r'],
    'SD': [side_5, edge_5, center_2, side_6, edge_6, '[SD] Shift cube down\r'],
    'RL': [side_3, edge_3, center_3, side_1, edge_1, '[RL] Rotate cube left\r'],
    'RR': [side_3, edge_3, center_3, side_1, edge_1, '[RR] Rotate cube right\r'],
    'S':  [CLEAR, ['cube.log', u_moves], 'Saving moves...', .5],
    'E':  [CLEAR, ['cube.log', u_moves], 'Exiting and saving moves...'],
    'Q':  [CLEAR, 'Quiting without saving...']
}
