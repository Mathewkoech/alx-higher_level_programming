#!/usr/bin/python3
"""
11;rgb:0000/0000/0000Lists all State objects
from the database hbtn_0e_6_usa.
"""

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access to the database
    """

    db = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    engine = create_engine(db)
    Session = sessionmaker(bind=engine)

    session = Session()

    for instance in session.query(State).filter(
            State.name.like('%a%')).order_by(State.id):
        print('{0}: {1}'.format(instance.id, instance.name))
