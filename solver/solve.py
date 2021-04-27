'''Rubik's solver functions'''

from solver.solve_1 import find_solution as find_cross
from solver.solve_2 import find_solution as find_corners
from solver.solve_3 import find_solution as find_edges
from solver.solve_4 import find_solution as find_top
from solver.solve_5 import find_solution as find_last


def solve_cube():
    '''Solve cube'''

    if find_cross():
        if find_corners():
            if find_edges():
                if find_top():
                    return find_last()
    return False
