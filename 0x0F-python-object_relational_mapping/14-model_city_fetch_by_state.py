#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from model_city import City
import sys


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
             sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)

    for city in session.query(State.name, City.id, City.name).filter(
                              State.id == City.state_id):
        print(city[0] + ": (" + str(city[1]) + ") " + city[2])
