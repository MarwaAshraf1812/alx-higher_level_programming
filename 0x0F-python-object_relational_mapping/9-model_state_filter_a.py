#!/usr/bin/python3
"""
Prints the first State object from the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

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

        state_withA = (
            session.query(State)
            .filter(State.name.like('%a%'))
            .order_by(State.id.asc())
            .all()
        )
        for state in state_withA:
            print(f"{state.id}: {state.name}")
        session.close()
