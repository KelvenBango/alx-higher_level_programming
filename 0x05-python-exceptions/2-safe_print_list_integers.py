#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count_integers = 0
    for index in range(x):
        try:
            print('{:d}'.format(my_list[index]), end='')
            count_integers += 1
        except IndexError:
            print('List index out of range')
        except (TypeError, ValueError):
            pass
    print()
    return count_integers
