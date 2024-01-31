#!/usr/bin/python3

"""module that prints square with #"""


def print_square(size):
    """
    Print a square of a specified size.

    Args:
    - size (int): The size of the square.

    Returns:
    - None
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        return

    for _ in range(size):
        print("#" * size)
