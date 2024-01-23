#!/usr/bin/python3

def no_c(my_string):
    new_string = ''
    first_char_to_remove = 'c'
    second_char_to_remove = 'C'

    for char in my_string:
        if char != first_char_to_remove and char != second_char_to_remove:
            new_string += char
    return new_string
