#!/usr/bin/python3
"""
Contains the class definition of a City
an instance Base = declarative_base().
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey
from model_state import Base

Base = declarative_base()


class City(Base):
    """
    City class that inherits from Base.
    Represents the Cities table in MySQL.
    """
    __tablename__ = "cities"
    id = Column(
        Integer,
        autoincrement=True,
        unique=True,
        nullable=False,
        primary_key=True
    )
    name = Column(
        String(length=128),
        nullable=False
    )
    state_id = Column(
        Integer,
        ForeignKey('states.id'),
        nullable=False
    )
