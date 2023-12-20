#!/usr/bin/python3
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
Base = declarative_base()


class State(Base):
    """State table class"""
    __tablename__ = "states"
    id = Column(Integer,
                primary_key=True,
                autoincrement=True,
                nullable=False
                )
    name = Column(String(128), nullable=False)
