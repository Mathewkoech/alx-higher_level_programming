#!/usr/bin/python3
"""module for append_write method"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8)
    Args:
        filename str()
        test str(): text added
    Returns the number of characters added.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(text)
        return len(text)
