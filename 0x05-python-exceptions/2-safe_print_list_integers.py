#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    try:
        for i in range(x):
            print('{:d}'.format(i[0]))

    except:
        continue

    print('\n')
    return x
