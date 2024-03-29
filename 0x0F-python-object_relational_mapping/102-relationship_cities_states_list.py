#!/usr/bin/python3
"""
lists all 'City' objects from the 'hbtn_0e_101_usa' database
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
    for c in session.query(City).order_by(City.id):
        print("{}: {} -> {}".format(c.id, c.name, c.state.name))
