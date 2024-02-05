#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count_items = 0
    for index in range(x):
        try:
            print('{}'.format(my_list[index]), end='')
            count_items += 1
        except IndexError:
            break
    print('')

    return count_items