#!/usr/bin/python3

"""module of write_file method"""


def write_file(filename="", text=""):
    """
    Writes text to a file and returns the number of characters written.

    Args:
        filename (str): The name of the text file.
        text (str): text to be written
    """
    with open(filename, 'w', encoding = 'utf-8')as file:
        content= file.write(text)
        return content
