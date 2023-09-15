#!/usr/bin/python3
"""
Write a Python file similar to model_state.py named model_city.py
that contains the class definition of a City.
"""
from model_state import Base
from sqlalchemy import Column, String, Integer, Sequence, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """
    Class definition of a City
    """
    __tablename__ = 'cities'

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

    state_id = Column(
        Integer,
        ForeignKey("states.id"),
        nullable=False
    )
