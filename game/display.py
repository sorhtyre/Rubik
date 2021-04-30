'''Cube display functions'''

from os import system as cli
from platform import system as arch

from data.cube import pieces

if arch() == 'Linux':
    R_ARROW = '▶'
    L_ARROW = '◀'
    CLEAR = 'clear'
else:
    R_ARROW = '►'
    L_ARROW = '◄'
    CLEAR = 'cls'


def set_color(tmp_string):
    '''Color encode text'''

    text_reset = '\033[0m'
    text_red = '\033[31m'
    text_green = '\033[32m'
    text_orange = '\033[33m'
    text_blue = '\033[34m'
    text_yellow = '\033[93m'

    if tmp_string == 'W':
        tmp_string = text_reset + tmp_string + text_reset
    elif tmp_string == 'G':
        tmp_string = text_green + tmp_string + text_reset
    elif tmp_string == 'Y':
        tmp_string = text_yellow + tmp_string + text_reset
    elif tmp_string == 'B':
        tmp_string = text_blue + tmp_string + text_reset
    elif tmp_string == 'R':
        tmp_string = text_red + tmp_string + text_reset
    elif tmp_string == 'O':
        tmp_string = text_orange + tmp_string + text_reset
    return tmp_string


def display():
    '''Display cube'''

    cli(CLEAR)
    print('                ' +
          set_color(pieces[18]) + '  ' +
          set_color(pieces[19]) + '  ' +
          set_color(pieces[20]) + '        ' +
          '[SR] Shift right    [SL] Shift left')
    print('                ' +
          set_color(pieces[21]) + '  ' +
          set_color(pieces[22]) + '  ' +
          set_color(pieces[23]) + '        ' +
          '[SU] Shift up       [SD] Shift down')
    print('                ' +
          set_color(pieces[24]) + '  ' +
          set_color(pieces[25]) + '  ' +
          set_color(pieces[26]) + '        ' +
          '[RR] Rotate right   [RL] Rotate left')
    print('\r')
    print('         ' + L_ARROW + '[ 9]  ' +
          set_color(pieces[9]) + '  ' +
          set_color(pieces[10]) + '  ' +
          set_color(pieces[11]) + '  [10]' + R_ARROW + '')
    print('                ' +
          set_color(pieces[12]) + '  ' +
          set_color(pieces[13]) + '  ' +
          set_color(pieces[14]))
    print('         ' + L_ARROW + '[11]  ' +
          set_color(pieces[15]) + '  ' +
          set_color(pieces[16]) + '  ' +
          set_color(pieces[17]) + '  [12]' + R_ARROW + '')
    print('\r')
    print('                ' + '▲     ▲')
    print('               ' + '[5]   [7]')
    print('\r')
    print(set_color(pieces[36]) + '  ' +
          set_color(pieces[37]) + '  ' +
          set_color(pieces[38]) + '   ' + L_ARROW + '[1]  ' +

          set_color(pieces[0]) + '  ' +
          set_color(pieces[1]) + '  ' +
          set_color(pieces[2]) + '  [2]' + R_ARROW + '  ' +

          set_color(pieces[45]) + '  ' +
          set_color(pieces[46]) + '  ' +
          set_color(pieces[47]))

    print(set_color(pieces[39]) + '  ' +
          set_color(pieces[40]) + '  ' +
          set_color(pieces[41]) + '         ' +

          set_color(pieces[3]) + '  ' +
          set_color(pieces[4]) + '  ' +
          set_color(pieces[5]) + '        ' +

          set_color(pieces[48]) + '  ' +
          set_color(pieces[49]) + '  ' +
          set_color(pieces[50]))

    print(set_color(pieces[42]) + '  ' +
          set_color(pieces[43]) + '  ' +
          set_color(pieces[44]) + '   ' + L_ARROW + '[3]  ' +

          set_color(pieces[6]) + '  ' +
          set_color(pieces[7]) + '  ' +
          set_color(pieces[8]) + '  [4]' + R_ARROW + '  ' +

          set_color(pieces[51]) + '  ' +
          set_color(pieces[52]) + '  ' +
          set_color(pieces[53]))
    print('\r')
    print('               ' + '[6]   [8]')
    print('                ' + '▼     ▼')
    print('\r')
    print('                ' +
          set_color(pieces[27]) + '  ' +
          set_color(pieces[28]) + '  ' +
          set_color(pieces[29]) + '        ' +
          '[U]ndo last move    [S]ave moves')
    print('                ' +
          set_color(pieces[30]) + '  ' +
          set_color(pieces[31]) + '  ' +
          set_color(pieces[32]) + '        ' +
          '[M]ix the cube      [E]xit and save moves')
    print('                ' +
          set_color(pieces[33]) + '  ' +
          set_color(pieces[34]) + '  ' +
          set_color(pieces[35]) + '        ' +
          '[R]eset the cube    [Q]uit without saving')
    print('\r')
