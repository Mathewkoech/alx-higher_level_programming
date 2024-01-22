#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """function that prints the first x elements
        of a list and only integers."""
    count = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end='')
            count += 1
        except (ValueError, TypeError):
            continue
        except IndexError:
            break
    print()
    return count
