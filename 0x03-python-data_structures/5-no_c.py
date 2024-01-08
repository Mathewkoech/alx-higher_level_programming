#!/usr/bin/python3
def no_c(my_string):
    """
    Removes letter c from a string

    """
    final_string = ""
    for i in range(len(my_string)):
        if (my_string[i] != 'c') and (my_string[i] != 'C'):
            final_string += my_string[i]
    return final_string
