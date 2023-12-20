#!/usr/bin/python3
'''
Displays all values in the states table of
hbtn_0e_0_usa where name matches the provided argument.

Parameters:
    - <user>: MySQL database username.
    - <password>: MySQL database password.
    - <database>: Name of the MySQL database.

Note: No argument validation needed.

Example:
    ./2-my_filter_states.py root root hbtn_0e_0_usa "Texas"
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
        query = 'SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC;'
        mycursor.execute(query, (state_name,))
        rows = mycursor.fetchall()
        for row in rows:
            print(row)
        mydb.close()
