'''Cube movement functions'''

from data.cube import pieces, default_pieces


def rotate_cw(section):
    '''Rotate Clockwise'''

    value = ['']*len(section)

    if len(section) == 9:
        for i, index in enumerate([6, 3, 0, 7, 4, 1, 8, 5, 2]):
            value[i] = pieces[section[index]]

        for i, index in enumerate(section):
            pieces[index] = value[i]
    else:
        for i, index in enumerate([9, 10, 11, 0, 1, 2, 3, 4, 5, 6, 7, 8]):
            value[i] = pieces[section[index]]

        for i, index in enumerate(section):
            pieces[index] = value[i]


def rotate_ccw(section):
    '''Rotate Counter-Clockwise'''

    value = ['']*len(section)

    if len(section) == 9:
        for i, index in enumerate([2, 5, 8, 1, 4, 7, 0, 3, 6]):
            value[i] = pieces[section[index]]

        for i, index in enumerate(section):
            pieces[index] = value[i]
    else:
        for i, index in enumerate([3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 1, 2]):
            value[i] = pieces[section[index]]

        for i, index in enumerate(section):
            pieces[index] = value[i]


def reset_cube():
    '''Reset the cube to default_pieces positions'''

    for i, _ in enumerate(pieces):
        pieces[i] = default_pieces[i]
