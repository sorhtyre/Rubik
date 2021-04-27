'''Rubik's solver functions'''

from solve_1 import find_solution as find_cross
from solve_2 import find_solution as find_corners
from solve_3 import find_solution as find_edges
from solve_4 import find_solution as find_top
from solve_5 import find_solution as find_last


def solve_cube():
    '''Solve cube'''

    if find_cross():
        if find_corners():
            if find_edges():
                if find_top():
                    return find_last()
    return False
