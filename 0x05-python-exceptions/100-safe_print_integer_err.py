#!/usr/bin/python3
from sys import stderr

def safe_print_integer_err(value):
    try:
        print('{:d}'.format(value))
    except (ValueError, TypeError) as err:
        return False
        print('Exception:{}'.format(err), file=stderr)

    print('\n')
    return True
