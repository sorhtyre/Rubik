'''Rubik's solver functions'''

from data.cube import pieces
from solver.si import do_move


def find_solution():
    '''Find solution'''

    tmp_edges = [[9, 10, 11], [47, 50, 53], [35, 34, 33], [42, 39, 36]]

    tmp_loop = True
    tmp_fail = False
    tmp_count = 0

    while tmp_loop:

        tmp_one = 0
        tmp_two = 0
        tmp_three = 0
        tmp_corners = 0

        for t_edge in tmp_edges:

            if pieces[t_edge[0]] != pieces[t_edge[1]] and \
               pieces[t_edge[0]] != pieces[t_edge[2]] and \
               pieces[t_edge[1]] != pieces[t_edge[2]]:
                tmp_one = tmp_one + 1

            elif (pieces[t_edge[0]] == pieces[t_edge[1]] and
                  pieces[t_edge[0]] != pieces[t_edge[2]]):
                tmp_two = tmp_two + 1
            elif (pieces[t_edge[1]] == pieces[t_edge[2]] and
                  pieces[t_edge[1]] != pieces[t_edge[0]]):
                tmp_two = tmp_two + 1
            elif (pieces[t_edge[0]] == pieces[t_edge[1]] and
                  pieces[t_edge[1]] == pieces[t_edge[2]]):
                tmp_three = tmp_three + 1
            elif (pieces[t_edge[0]] == pieces[t_edge[2]] and
                  pieces[t_edge[0]] != pieces[t_edge[1]]):
                tmp_corners = tmp_corners + 1

        if tmp_three == 4:
            tmp_loop = False

        if tmp_three > 0 and tmp_corners < 3:
            solve_three()

        if tmp_two > 0 and tmp_corners == 0:
            solve_two()

        if tmp_one == 4:
            solve_one()

        if tmp_corners > 0:
            solve_corners()

        tmp_count = tmp_count + 1
        if tmp_count > 15:
            return tmp_fail

    return True


def debug_image():
    '''Debug image'''

    print('')
    print("    " + pieces[18] + pieces[19] + pieces[20] + "    ")
    print("    " + pieces[21] + pieces[22] + pieces[23] + "    ")
    print("    " + pieces[24] + pieces[25] + pieces[26] + "    ")
    print("    " + pieces[9] + pieces[10] + pieces[11] + "    ")
    print("    " + pieces[12] + pieces[13] + pieces[14] + "    ")
    print("    " + pieces[15] + pieces[16] + pieces[17] + "    ")
    print(pieces[36] + pieces[37] + pieces[38] + " " +
          pieces[0] + pieces[1] + pieces[2] + " " +
          pieces[45] + pieces[46] + pieces[47])
    print(pieces[39] + pieces[40] + pieces[41] + " " +
          pieces[3] + pieces[4] + pieces[5] + " " +
          pieces[48] + pieces[49] + pieces[50])
    print(pieces[42] + pieces[43] + pieces[44] + " " +
          pieces[6] + pieces[7] + pieces[8] + " " +
          pieces[51] + pieces[52] + pieces[53])
    print("    " + pieces[27] + pieces[28] + pieces[29] + "    ")
    print("    " + pieces[30] + pieces[31] + pieces[32] + "    ")
    print("    " + pieces[33] + pieces[34] + pieces[35] + "    ")
    print('')


def solve_one():
    '''Solve one'''

    if pieces[9] == 'G':
        find_2()
    elif pieces[9] == 'O':
        find_1()
    elif pieces[9] == 'B':
        find_0()
    else:
        find_3()


def solve_two():
    '''Solve two'''

    tmp_edges = [[9, 10, 11], [47, 50, 53], [35, 34, 33], [42, 39, 36]]

    for t_index, t_edge in enumerate(tmp_edges):

        if pieces[t_edge[0]] == pieces[t_edge[1]] and \
           pieces[t_edge[0]] != pieces[t_edge[2]]:
            move_edge(t_index, t_edge)

            if pieces[t_edge[0]] == 'G':
                find_0()
            elif pieces[t_edge[0]] == 'O':
                find_3()
            elif pieces[t_edge[0]] == 'B':
                find_2()
            else:
                find_1()
            break

        if pieces[t_edge[1]] == pieces[t_edge[2]] and \
           pieces[t_edge[1]] != pieces[t_edge[0]]:
            move_edge(t_index, t_edge)

            if pieces[t_edge[1]] == 'G':
                find_3()
            elif pieces[t_edge[1]] == 'O':
                find_2()
            elif pieces[t_edge[1]] == 'B':
                find_1()
            else:
                find_0()
            break


def solve_corners():
    '''Solve corners'''

    tmp_edges = [[9, 10, 11], [47, 50, 53], [35, 34, 33], [42, 39, 36]]

    for t_index, t_edge in enumerate(tmp_edges):

        if pieces[t_edge[0]] == pieces[t_edge[2]] and \
           pieces[t_edge[0]] != pieces[t_edge[1]]:

            tmp_count = 0
            for i_edge in tmp_edges:

                if pieces[i_edge[0]] == pieces[i_edge[2]]:
                    tmp_count = tmp_count + 1

            if tmp_count == 4:
                move_edge(t_index, t_edge)

                if pieces[9] == pieces[39]:
                    find_mid_0(0)
                elif pieces[9] == pieces[50]:
                    find_mid_0(1)
                elif pieces[36] == pieces[10]:
                    find_mid_2(0)
                elif pieces[36] == pieces[34]:
                    find_mid_2(1)
                elif pieces[47] == pieces[10]:
                    find_mid_3(0)
                elif pieces[47] == pieces[34]:
                    find_mid_3(1)
                elif pieces[33] == pieces[39]:
                    find_mid_1(0)
                elif pieces[33] == pieces[50]:
                    find_mid_1(1)
                else:
                    find_mid_0(0)

                break

            if tmp_count == 1:
                move_edge(t_index, t_edge)

                if pieces[t_edge[0]] == 'G':
                    find_0()
                elif pieces[t_edge[0]] == 'O':
                    find_3()
                elif pieces[t_edge[0]] == 'B':
                    find_2()
                else:
                    find_1()

                break


def solve_three():
    '''Solve three'''

    tmp_edges = [[9, 10, 11], [47, 50, 53], [35, 34, 33], [42, 39, 36]]

    for t_index, t_edge in enumerate(tmp_edges):

        if pieces[t_edge[0]] == pieces[t_edge[1]] and \
           pieces[t_edge[1]] == pieces[t_edge[2]]:

            tmp_count = 0
            for i_edge in tmp_edges:

                if pieces[i_edge[0]] == pieces[i_edge[1]] and \
                   pieces[i_edge[1]] == pieces[i_edge[2]]:
                    tmp_count = tmp_count + 1

            if tmp_count == 4:
                move_edge(t_index, t_edge)
                break

            tmp_count = 0
            for i_edge in tmp_edges:

                if pieces[i_edge[0]] == pieces[i_edge[2]]:
                    tmp_count = tmp_count + 1

            if tmp_count == 4:
                move_edge(t_index, t_edge)

                if pieces[9] == pieces[39]:
                    find_mid_0(0)
                elif pieces[9] == pieces[50]:
                    find_mid_0(1)
                elif pieces[33] == pieces[39]:
                    find_mid_1(0)
                elif pieces[33] == pieces[50]:
                    find_mid_1(1)
                else:
                    find_mid_0(0)

                break

            move_edge(t_index, t_edge)

            if pieces[t_edge[0]] == 'G':
                find_0()
            elif pieces[t_edge[0]] == 'O':
                find_3()
            elif pieces[t_edge[0]] == 'B':
                find_2()
            else:
                find_1()

            break


def move_edge(tmp_index, tmp_edge):
    '''Move edge'''

    if pieces[tmp_edge[0]] == 'G':
        if tmp_index == 1:
            do_move('9')
        elif tmp_index == 2:
            do_move('9')
            do_move('9')
        elif tmp_index == 3:
            do_move('10')

    elif pieces[tmp_edge[0]] == 'O':
        if tmp_index == 2:
            do_move('9')
        elif tmp_index == 3:
            do_move('9')
            do_move('9')
        elif tmp_index == 0:
            do_move('10')

    elif pieces[tmp_edge[0]] == 'B':
        if tmp_index == 3:
            do_move('9')
        elif tmp_index == 0:
            do_move('9')
            do_move('9')
        elif tmp_index == 1:
            do_move('10')

    elif pieces[tmp_edge[0]] == 'R':
        if tmp_index == 0:
            do_move('9')
        elif tmp_index == 1:
            do_move('9')
            do_move('9')
        elif tmp_index == 2:
            do_move('10')


def find_0():
    '''Blue face'''

    do_move('5')
    do_move('4')
    do_move('5')
    do_move('1')
    do_move('1')
    do_move('6')
    do_move('3')
    do_move('5')
    do_move('1')
    do_move('1')
    do_move('6')
    do_move('6')


def find_1():
    '''Orange face'''

    do_move('3')
    do_move('7')
    do_move('3')
    do_move('6')
    do_move('6')
    do_move('4')
    do_move('8')
    do_move('3')
    do_move('6')
    do_move('6')
    do_move('4')
    do_move('4')


def find_2():
    '''Green face'''

    do_move('8')
    do_move('1')
    do_move('8')
    do_move('4')
    do_move('4')
    do_move('7')
    do_move('2')
    do_move('8')
    do_move('4')
    do_move('4')
    do_move('7')
    do_move('7')


def find_3():
    '''Red face'''

    do_move('2')
    do_move('6')
    do_move('2')
    do_move('7')
    do_move('7')
    do_move('1')
    do_move('5')
    do_move('2')
    do_move('7')
    do_move('7')
    do_move('1')
    do_move('1')


def find_mid_0(tmp_bool):
    '''Find mid green'''

    do_move('1')
    do_move('1')
    if tmp_bool == 0:
        do_move('10')
    else:
        do_move('9')
    do_move('8')
    do_move('6')
    do_move('1')
    do_move('1')
    do_move('5')
    do_move('7')
    if tmp_bool == 0:
        do_move('10')
    else:
        do_move('9')
    do_move('1')
    do_move('1')


def find_mid_1(tmp_bool):
    '''Find mid blue'''

    do_move('4')
    do_move('4')
    if tmp_bool == 0:
        do_move('10')
    else:
        do_move('9')
    do_move('5')
    do_move('7')
    do_move('4')
    do_move('4')
    do_move('8')
    do_move('6')
    if tmp_bool == 0:
        do_move('10')
    else:
        do_move('9')
    do_move('4')
    do_move('4')


def find_mid_2(tmp_bool):
    '''Find mid red'''

    do_move('6')
    do_move('6')
    if tmp_bool == 0:
        do_move('9')
    else:
        do_move('10')
    do_move('2')
    do_move('4')
    do_move('6')
    do_move('6')
    do_move('1')
    do_move('3')
    if tmp_bool == 0:
        do_move('9')
    else:
        do_move('10')
    do_move('6')
    do_move('6')


def find_mid_3(tmp_bool):
    '''Find mid orange'''

    do_move('7')
    do_move('7')
    if tmp_bool == 0:
        do_move('10')
    else:
        do_move('9')
    do_move('1')
    do_move('3')
    do_move('7')
    do_move('7')
    do_move('2')
    do_move('4')
    if tmp_bool == 0:
        do_move('10')
    else:
        do_move('9')
    do_move('7')
    do_move('7')
