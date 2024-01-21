#!/usr/bin/python3

def remove_char_at(str, n):
    for character_array in str:
        if n < 0:
            return str
        return character_array[:n] + character_array[n + 1:]
