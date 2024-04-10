#!/usr/bin/python3
"""
script that lists all cities from the database hbtn_0e_4_usa
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
    with db_connect.cursor() as db_cursor:
        # Execute SQL query to retrieve cities of the specified state
        db_cursor.execute("""
            SELECT
                cities.id, cities.name
            FROM
                cities
            JOIN
                states
            ON
                cities.state_id = states.id
            WHERE
                states.name LIKE BINARY %(state_name)s
            ORDER BY
                cities.id ASC
        """, {
            'state_name': argv[4]
        })
        # Fetchind data
        cities_selected = db_cursor.fetchall()

    # Print the names of cities for  rows are selected
    if cities_selected is not None:
        print(", ".join([row[1] for row in cities_selected]))
