#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10
message = 'and is 0' if last_digit == 0 else 
        ('and is greater than 5' if last_digit > 5 else 
                'and is less than 6 and not 0')

print(f'Last digit of {number} is {last_digit} {message}')
