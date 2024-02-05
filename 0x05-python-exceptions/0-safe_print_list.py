#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        count_items = 0
        for list_item in my_list:
            print('{}'.format(list_item), end='')
            count_items+=1
        return count_items
    except:
        print('Exception occured')
