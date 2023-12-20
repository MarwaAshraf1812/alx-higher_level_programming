#!/usr/bin/python3
"""
Contains the class definition of a State 
an instance Base = declarative_base().
"""


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
Base = declarative_base()


class State(Base):
    """
    State class that inherits from Base.
    Represents the states table in MySQL.
    """
    __tablename__ = "states"
    id = Column(Integer,
                primary_key=True,
                autoincrement=True,
                nullable=False
                )
    name = Column(String(128), nullable=False)
