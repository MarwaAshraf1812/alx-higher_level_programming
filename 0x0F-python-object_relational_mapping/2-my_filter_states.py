#!/usr/bin/python3
'''
Displays all values in the states table of 
hbtn_0e_0_usa where name matches the provided argument.

Parameters:
    - <username>: MySQL database username.
    - <password>: MySQL database password.
    - <database>: Name of the MySQL database.
    - <state_name>: Name of the state to search for.

Note: No argument validation needed.

Example:
    ./2-my_filter_states.py root root hbtn_0e_0_usa Texas
'''

import sys
import MySQLdb

if __name__ == '__main__':
    if len(sys.argv) >= 4:
        mydb = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            password=sys.argv[2],
            database=sys.argv[3]
        )
        mycursor = mydb.cursor()
        query="SELECT * FROM states WHERE name LIKE %s ORDER by id ASC"
        user_input = (sys.argv[4],)
        mycursor.execute(query, user_input)

        rows = mycursor.fetchall()

        for row in rows:
            print(row)
        mydb.close()
