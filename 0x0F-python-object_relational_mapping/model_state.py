#!/usr/bin/python3
"""
Write a python file that contains the class definition of a State
and an instance Base = declarative_base()
"""
from sqlalchemy import Column, String, Integer, Sequence, MetaData
from sqlalchemy.ext.declarative import declarative_base

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


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
