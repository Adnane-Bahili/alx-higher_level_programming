#!/usr/bin/python3
"""
lists all 'State' objects that contain the letter 'a'
from the 'hbtn_0e_6_usa' database
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    access to the database and get the states from the database
    """
    database_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(database_url)
    Session = sessionmaker(bind=engine)
    session = Session()
    for si in session.query(State).filter(State.name.contains('a')):
        print('{0}: {1}'.format(si.id, si.name))
