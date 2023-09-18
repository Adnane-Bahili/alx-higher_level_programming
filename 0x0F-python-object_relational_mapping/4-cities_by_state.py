#!/usr/bin/python3
"""
lists all cities from the 'hbtn_0e_4_usa' database
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
        current.execute("""SELECT cities.id, cities.name, states.name
                           FROM cities
                           JOIN states ON cities.state_id = states.id
                           ORDER BY cities.id ASC""")
        rows = current.fetchall()
    if rows is not None:
        for r in rows:
            print(r)
