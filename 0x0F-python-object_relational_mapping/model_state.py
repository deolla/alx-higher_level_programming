#!/usr/bin/python3
"""
Write a python file that contains the class definition of a State
and an instance Base = declarative_base()
"""
from sqlalchemy import Column, String, Integer, Sequence
from sqlalchemy.ext.declarative import declarative_base

metdata = MetaData()
Base = declarative_base(metadata=metdata)


class State(Base):
    """
    Contains the class definition of a State and an instance of base
    """
    __tablename__ = 'states'

    id = Column(
        Integer,
        autoincrement=True,
        nullable=False,
        primary_key=True
    )

    name = Column(
        String(128),
        nullable=False
    )

    def __init__(self, id, name):
        """
        Inherit from class

        Args:
            id - represents a column of an auto-generated, unique integer,
                 can’t be null and is a primary key.
            name - represents a column of a string with maximum 128 characters
                   and can’t be null.
        """
        if id is not None:
            self.id = id
        self.name = name
