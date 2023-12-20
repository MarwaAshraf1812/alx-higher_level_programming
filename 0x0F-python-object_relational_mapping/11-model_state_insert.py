#!/usr/bin/python3
"""
Adds the State object “Louisiana” to the database hbtn_0e_6_usa.
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

        newState = State(name='Louisiana')
        session.add(newState)
        session.commit()

        print(newState.id)

        session.close()
