#!/usr/bin/python3

if __name__ == '__main__':
    import sys

    arg_length = len(sys.argv) - 1
    result = 0
    for number in range(arg_length):
        result += int(sys.argv[number + 1])
    print(f'{result}')
