#!/usr/bin/python3
"""
Write a script that lists all City objects from the database hbtn_0e_101_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import relationship
import sys


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
             sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)

    for m in session.query(State).order_by(State.id).all():
        for i in m.cities:
            print(f"{i.id}: {i.name} -> {m.name}")
    session.close()
