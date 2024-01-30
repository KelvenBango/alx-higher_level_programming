#!/usr/bin/python3
from functools import reduce

def uniq_add(my_list=[]):
    unique_list = list(set(my_list))
    new_list = reduce(lambda x, y: x + y, unique_list)
    return new_list
