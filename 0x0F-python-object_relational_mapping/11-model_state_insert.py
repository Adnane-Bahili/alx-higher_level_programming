#!/usr/bin/python3
"""
adds the State object 'Louisiana' to the 'hbtn_0e_6_usa' database
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
    lou_state = State(name='Louisiana')
    session.add(lou_state)
    session.commit()
    print('{0}'.format(lou_state.id))
    session.close()
