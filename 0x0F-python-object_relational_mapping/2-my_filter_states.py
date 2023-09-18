#!/usr/bin/python3
"""
takes in an argument and displays all values in the states
where 'name' matches the argument from the 'hbtn_0e_0_usa' database
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    access to the database and get the states from the database
    """
    database = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                               password=argv[2], db=argv[3])
    current = database.cursor()
    current.execute("SELECT * FROM states\
                    WHERE name LIKE BINARY '{}'\
                    ORDER BY states.id ASC".format(argv[4]))
    rows = current.fetchall()
    for r in rows:
        print(r)
