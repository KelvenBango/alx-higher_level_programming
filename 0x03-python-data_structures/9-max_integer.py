#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) <= 0:
        return None
    else:
        max_number = my_list[0]
        for index in range(len(my_list)):
            if my_list[index] > max_number:
                max_number = my_list[index]
        return max_number
