#!/usr/bin/python3
"""
Improve the model_state.py, and save as relationship_state.py
"""
from sqlalchemy import Column, String, Integer, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


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

    cities = relationship(
        "City",
        backref="states"
    )
