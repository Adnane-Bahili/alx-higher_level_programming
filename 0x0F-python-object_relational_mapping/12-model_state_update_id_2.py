#!/usr/bin/python3
"""
changes the name of a 'State' object from the database 'hbtn_0e_6_usa'
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    updates a 'State' object on the database
    """
    database_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(database_url)
    Session = sessionmaker(bind=engine)
    session = Session()
    ari_state = session.query(State).filter(State.id == '2').first()
    ari_state.name = 'New Mexico'
    session.commit()
    session.close()
