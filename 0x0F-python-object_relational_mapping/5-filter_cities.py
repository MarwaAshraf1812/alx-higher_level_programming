#!/usr/bin/python3
'''
Lists all cities of a given state from the database hbtn_0e_4_usa

Parameters:
    - <username>: MySQL database username.
    - <password>: MySQL database password.
    - <database>: Name of the MySQL database.
    - <state_name>: Name of the state.

Note: No argument validation needed.

Example:
    ./5-filter_cities.py root root hbtn_0e_4_usa Texas
'''

import sys
import MySQLdb

if __name__ == '__main__':
    if len(sys.argv) == 5:
        mydb = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            password=sys.argv[2],
            database=sys.argv[3]
        )
        mycursor = mydb.cursor()
        state_name = sys.argv[4]
        mycursor.execute(
            'SELECT cities.name FROM cities' +
            ' INNER JOIN states ON cities.state_id = states.id' +
            ' WHERE CAST(states.name AS BINARY) = %s' +
            ' ORDER BY cities.id ASC;',
            [state_name]
        )
        rows = mycursor.fetchall()
        for row in rows:
            print(row)
        mydb.close()
