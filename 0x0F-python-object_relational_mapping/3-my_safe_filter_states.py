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
    with database.cursor() as current:
        current.execute("""SELECT * FROM states WHERE name LIKE BINARY %(name)s
                        ORDER BY states.id ASC """, {'name': argv[4]})
        rows = current.fetchall()
    if rows is not None:
        for r in rows:
            print(r)
