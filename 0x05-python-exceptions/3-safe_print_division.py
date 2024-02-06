#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        integer_division = a / b
    except ZeroDivisionError:
        integer_division = None
    finally:
        print('Inside result: {}'.format(integer_division))
        return integer_division
