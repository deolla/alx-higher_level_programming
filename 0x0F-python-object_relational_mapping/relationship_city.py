#!/usr/bin/python3
"""
Improve the files model_city.py and model_state.py, and save them as
relationship_city.py and relationship_state.py
"""
from relationship_state import Base
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
