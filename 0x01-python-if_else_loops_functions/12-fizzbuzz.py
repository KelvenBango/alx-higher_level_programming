#!/usr/bin/python3

def fizzbuzz():
    """
    Prints the numbers from 1 to 100 separeted by a space
        
        * For multiples of three print 'Fizz'instead of the number
          and for multiples of five print 'Buzz'
        * For numbers which are multiples of both three and five print FizzBuzz
        * Each element should be followed by a space
    """

    for number in range(1, 101):
        
        if number % 3 == 0 and number % 5 == 0:
            print('FizzBuzz', end=' ')
        elif number % 3 == 0:
            print('Fizz', end=' ')
        elif number % 5 == 0:
            print('Buzz', end=' ')
        else: 
            print(f'{number}', end=' ')

fizzbuzz()
