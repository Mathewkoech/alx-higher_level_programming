#!/usr/bin/python3
"""
This script lists all states from the database `hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv


def main():
    """
    Function to access the database and retrieve the states.
    """
    # Connection to the database
    db_connect = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])

    # Cursor object to execute SQL queries
    db_cursor = db_connect.cursor()

    # SQL query to select all states
    db_cursor.execute("SELECT * FROM states")

    # Fetch all rows selected by the query
    states_selected = db_cursor.fetchall()

    # Print each row
    for states in states_selected:
        print(states)


if __name__ == '__main__':
    # Call the main function when the script is executed
    main()
