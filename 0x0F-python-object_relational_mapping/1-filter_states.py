#!/usr/bin/python3
"""
This script lists all states with
a `name` starting with the letter `N`
from the database `hbtn_0e_0_usa`.
"""


import MySQLdb
from sys import argv


if __name__ == '__main__':
    """
    Access the database and retrieve the states.
    """
    # Connection to the database
    db_connect = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])

    # Cursor object to execute SQL queries
    db_cursor = db_connect.cursor()

    # SQL query to select all states
    db_cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY states.id ASC")

    # Fetch all rows selected by the query
    states_selected = db_cursor.fetchall()

    # Print each row
    for states in states_selected:
        print(states)
