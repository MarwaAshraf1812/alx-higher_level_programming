#!/usr/bin/python3
'''
Lists all states from the database hbtn_0e_0_usa.

Usage:
    ./0-select_states.py <username> <password> <database>

Parameters:
    - <username>: MySQL database username.
    - <password>: MySQL database password.
    - <database>: Name of the MySQL database.

Note: No argument validation needed.

Example:
    ./0-select_states.py root root hbtn_0e_0_usa
'''

import sys
import MySQLdb

if __name__ == '__main__':
    if len(sys.argv) == 4:
        mydb = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            password=sys.argv[2],
            database=sys.argv[3]
        )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM states ORDER BY id ASC;")

        rows = mycursor.fetchall()

        for row in rows:
            print(row)
        mydb.close()
