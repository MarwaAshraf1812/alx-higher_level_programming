#!/usr/bin/python3
'''
Lists all cities from the database hbtn_0e_4_usa

Parameters:
    - <username>: MySQL database username.
    - <password>: MySQL database password.
    - <database>: Name of the MySQL database.

Note: No argument validation needed.

Example:
    ./4-cities_by_state.py root root hbtn_0e_4_usa
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
        state_input = sys.argv[4]
        mycursor.execute(
            'SELECT  cities.name FROM cities ' +
            'INNER JOIN states ON cities.state_id = states.id ' +
            'WHERE CAST(states.name AS BINARY)=%s' +
            'ORDER BY cities.id ASC;',
            [state_input]
        )
        rows = mycursor.fetchall()
        for row in rows:
            print(row)
        mydb.close()
