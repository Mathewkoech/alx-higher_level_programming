#!/usr/bin/python3
"""
module for text_indentation method
"""


def text_indentation(text):
    """Print text with two new lines after each '.' , '?', ':'

    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    parameters = ['.', '?', ':']
    current_line = ""

    for char in text:  # iterate each character in text
        current_line += char  # append character

        # check if the character is present in parameters list
        if char in parameters:
            print(current_line.strip() + '\n')
            current_line = ""

    if current_line:
        print(current_line.strip())
