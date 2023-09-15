#!/usr/bin/python3
"""
Write a script that deletes all State objects with a name containing the
letter a from the database hbtn_0e_6_usa.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
import sys


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
             sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)

    for state in session.query(State).filter(State.name.like('%a%')).all():
        session.delete(state)

    session.commit()
