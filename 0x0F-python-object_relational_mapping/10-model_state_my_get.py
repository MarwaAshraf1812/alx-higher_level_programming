#!/usr/bin/python3
"""
Prints the State object with the name passed
as an argument from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    if len(sys.argv) == 5:
        user = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        search = sys.argv[4]

        engine = create_engine(
            "mysql://{}:{}@localhost:3306/{}".format(user, password, database)
        )

        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()

        try:
            state = session.query(State).filter_by(name=search).first()

            if state:
                print(state.id)
            else:
                print("Not found")

        except Exception as e:
            print("Error:", e)

        finally:
            session.close()
