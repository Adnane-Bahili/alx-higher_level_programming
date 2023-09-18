#!/usr/bin/python3
"""
takes in the name of a state as an argument and lists all cities of that state
using the 'hbtn_0e_4_usa' database
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
        current.execute("""SELECT cities.id, cities.name FROM cities
                           JOIN states ON cities.state_id = states.id
                           WHERE states.name LIKE BINARY %(state_name)s
                           ORDER BY cities.id ASC""", {'state_name': argv[4]})
        rows = current.fetchall()
    if rows is not None:
        print(", ".join([r[1] for r in rows]))
