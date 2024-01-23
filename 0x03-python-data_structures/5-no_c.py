#!/usr/bin/python3

def no_c(my_string):
    new_string = ''
    first_char_to_remove = 'c'
    second_char_to_remove = 'C'

    for character in my_string:
        if character != first_char_to_remove and character != second_char_to_remove:
            new_string += character
    return new_string
