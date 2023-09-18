#!/usr/bin/python3
"""lists all the states from the database"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    database = MySQLdb.connect(host="localhost", port=3306,
                               user=argv[1], password=argv[2], db=argv[3])
    current = database.cursor()
    number_rows = current.execute("SELECT * FROM states ORDER BY states.id")
    for r in range(number_rows):
        print(current.fetchone())
