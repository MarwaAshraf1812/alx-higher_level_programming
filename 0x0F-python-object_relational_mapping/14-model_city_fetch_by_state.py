#!/usr/bin/python3
'''Prints all City objects from the database hbtn_0e_14_usa.
'''
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    if len(sys.argv) == 4:
        user = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]

        engine = create_engine(
            "mysql://{}:{}@localhost:3306/{}".format(user, password, database)
        )

        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()

        for instance in (session.query(State.name, City.id, City.name)
                         .filter(State.id == City.state_id)):
            print(instance[0] + ": (" + str(instance[1]) + ") " + instance[2])
        session.close()
