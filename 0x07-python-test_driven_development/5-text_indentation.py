#!/usr/bin/python3

"""Text Indentation
This module provides a funcion that prints a text with 2 new lines after each characters.

Function:
    text_indentation(text): prints a text with 2 new lines after each of these characters `. ? :`
"""

def text_indentation(text):
    """Prints a text with 2 new lines after each characters

    Args:
        text (str): the text to be printed

    Raises:
        TypeError: If the text is not a string raises a exception with the message `text must be a string`
    """

    if not isinstance(text, str):
        raise TypeError('text must be a string')

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
