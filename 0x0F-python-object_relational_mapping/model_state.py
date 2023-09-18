#!/usr/bin/python3
"""
defines a 'State' class and a 'Base' class to work with  the MySQLAlchemy ORM
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class State(Base):
    """ 'State' class
    attributes:
        __tablename__ (str): class table name
        id (int): class id
        name (str): class name
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
