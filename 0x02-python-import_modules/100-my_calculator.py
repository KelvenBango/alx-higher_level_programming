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
    first_number = int(sys.argv[1])
    second_number = int(sys.argv[3])

    if operator not in available_operators:
        print(f'Unknown operator. Available operators: +, -, * and /')
        sys.exit(1)
    if operator == '+':
        print(f'{first_number} + {second_number} = \
                {add(first_number, second_number)}')
    elif operator == '-':
        print(f'{first_number} - {second_number} = \
                {sub(first_number, second_number)}')
    elif operator == '/':
        print(f'{first_number} / {second_number} = \
                {div(first_number, second_number)}')
    else:
        print(f'{first_number} * {second_number} = \
                {mul(first_number, second_number)}')
