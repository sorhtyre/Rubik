'''Find functions'''

#from interface import do_move
from cube import pieces


def find_centers():
    '''Find centers'''

    if pieces[4] != 'W':
        if pieces[13] == 'W':
            do_move('SD')
        elif pieces[22] == 'W':
            do_move('')
        elif pieces[31] == 'W':
            do_move('')
        elif pieces[40] == 'W':
            do_move('')
        elif pieces[49] == 'W':
            do_move('')

#        if pieces[13] == 'G':
#            if pieces[22] == 'Y':
#                if pieces[31] == 'B':
#                    if pieces[40] == 'R':
#                        if pieces[49] == 'O':
#                            print('centers are home')
