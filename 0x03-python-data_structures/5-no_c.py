#!/usr/bin/python3

def no_c(my_string):
    new_string = ''
    char_to_remove = 'c'

    for character in my_string:
        if character != char_to_remove:
            new_string += character
    return new_string
