#!/usr/bin/python3
"""
lists all the 'State' objects and corresponding 'City' objects contained
in the database 'hbtn_0e_101_usa'
arguments:
    mysql username (str)
    mysql password (str)
    database name (str)
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    for s in session.query(State).order_by(State.id):
        print("{}: {}".format(s.id, s.name))
        for c in s.cities:
            print("    {}: {}".format(c.id, c.name))
