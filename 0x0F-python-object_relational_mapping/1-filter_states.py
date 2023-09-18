#!/usr/bin/python3
"""
lists all the  states
with a 'name' starting with 'N'
from the 'hbtn_0e_0_usa' database
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    access to the database and gets the states from the database
    """
    database = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                               password=argv[2], db=argv[3])
    current = database.cursor()
    current.execute("SELECT * FROM states \
            WHERE name LIKE BINARY 'N%' \
            ORDER BY states.id ASC")
    rows = current.fetchall()
    for r in rows:
        print(r)
