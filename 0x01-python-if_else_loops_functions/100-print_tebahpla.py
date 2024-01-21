#!/usr/bin/python3

for alphabet in range(ord('z'), ord('a') - 1, -1):
    if alphabet % 2 == 0:
        difference = 0
    else:
        difference = 32
    print('{}'.format(chr(alphabet - difference)), end='')
