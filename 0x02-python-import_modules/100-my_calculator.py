#!/usr/bin/python3

if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    import sys

    arg_length = len(sys.argv) - 1

    if arg_length != 3:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        sys.exit(1)

    available_operators = ['+', '-', '*', '/']
    operator = sys.argv[2]
    first = int(sys.argv[1])
    second = int(sys.argv[3])

    if operator not in available_operators:
        print('Unknown operator. Available operators: +, -, * and /')
        sys.exit(1)
    if operator == '+':
        print('{} + {} = {}'.format(first, second, add(first, second)))
    elif operator == '-':
        print('{} - {} = {}'.format(first, second, sub(first, second)))
    elif operator == '/':
        print('{} / {} = {}'.format(first, second, div(first, second)))
    elif operator == '*':
        print('{} * {} = {}'.format(first, second, mul(first, second)))
