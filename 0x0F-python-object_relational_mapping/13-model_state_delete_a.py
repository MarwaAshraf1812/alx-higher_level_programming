#!/usr/bin/python3
'''Deletes all State objects with 'a' in its name in a database.
'''
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State

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
        deletedata = session.query(State).filter(State.name.like('%a%')) \
            .delete(synchronize_session=False)
        session.commit()
        session.close()
