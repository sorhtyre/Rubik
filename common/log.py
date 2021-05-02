'''Log functions'''

import os


def check_log(tmp_file):
    '''Check the log file'''
    if os.path.isfile(tmp_file):
        if os.stat(tmp_file).st_size > 0:
            return True
    return False


def write_log(tmp_list):
    '''Write move to log'''

    file_handle = open(tmp_list[0], 'w')
    file_handle.writelines(tmp_list[1])
    file_handle.close()


def read_log(tmp_file):
    '''Read the log file'''

    tmp_log = []

    if check_log(tmp_file):
        file_handle = open(tmp_file, 'r')
        tmp_log = file_handle.readlines()
        file_handle.close()
    return tmp_log


def reset_log(tmp_file):
    '''Clear the log file'''

    file_handle = open(tmp_file, 'w')
    file_handle.truncate(0)
    file_handle.close()
