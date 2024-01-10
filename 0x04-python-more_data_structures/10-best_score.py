#!/usr/bin/python3

def best_score(a_dictionary):
    """
    Returns the key with the biggest integer value in the dictionary.

    Args:
        a_dictionary (dict): Input dictionary.

   Returns:
        str: The key with the biggest integer value, or None
    """
    if a_dictionary is None:
        return None

    biggest_value_key = max(a_dictionary, key=lambda k: a_dictionary[k])
    return biggest_value_key
