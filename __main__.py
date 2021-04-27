'''Rubik's Text'''

import sys

from game.display import display
from game.ui import load_move, do_move

# Verify Python version
if sys.version_info[0] < 3:
    print('This app requires Python 3')
    sys.exit()


def main():
    '''Main function'''

    user_input = ''
    load_move()

    while user_input != 'Q' or user_input != 'q':
        do_move(user_input.upper())
        display()
        user_input = input()


if __name__ == '__main__':
    main()
