'''Log functions'''

import os

FILENAME = 'solve.log'


def check_log():
    '''Check the log file'''
    if os.path.isfile(FILENAME):
        if os.stat(FILENAME).st_size > 0:
            return True
    return False


def write_log_item(tmp_msg):
    '''Write move to log'''

    file_handle = open(FILENAME, 'a')
    file_handle.write(tmp_msg)
    file_handle.close()


def delete_log_item():
    '''Delete a line from the log file'''

    if check_log():
        line_list = read_log()[:-2]
        file_handle = open(FILENAME, 'w')
        for tmp_line in line_list:
            file_handle.write(tmp_line)
        file_handle.close()


def read_log():
    '''Read the log file'''

    if check_log():
        file_handle = open(FILENAME, 'r')
        line_list = file_handle.readlines()
        file_handle.close()
        return line_list
    return ''


def reset_log():
    '''Clear the log file'''

    file_handle = open(FILENAME, 'w')
    file_handle.truncate(0)
    file_handle.close()
