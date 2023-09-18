#!/usr/bin/python3
"""
prints the 'State' object id, with the name passed as argument
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
    si = session.query(State).filter(State.name == argv[4]).first()
    if si is None:
        print('Not found')
    else:
        print('{0}'.format(si.id))
