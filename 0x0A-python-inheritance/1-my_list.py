#!/usr/bin/python3
"""1-my_list moodule
This module provides a class MyList that inherits from List.

Functions:
    print_sorted(self): Prints the list, but sorted(ascending sort)
"""


class MyList(list):
    """MyList class that inherits from list"""

    def print_sorted(self):
        """Print the list, but sorted(ascending sort)"""
        print(sorted(self))
