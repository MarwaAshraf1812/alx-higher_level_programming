#!/usr/bin/python3
'''
Prints all rows in the states table of a database.

Usage:
    python script.py <username> <password> <database>

Parameters:
    - <user>: MySQL database username.
    - <password>: MySQL database password.
    - <database>: Name of the MySQL database.

Example:
    python script.py myuser mypassword mydatabase
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
mycursor.execute("SELECT * FROM states ORDER BY id ASC;")
rows = mycursor.fetchall()
for row in rows:
    print(row)
mydb.close()
