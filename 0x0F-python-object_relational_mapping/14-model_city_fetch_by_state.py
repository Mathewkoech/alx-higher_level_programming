#!/usr/bin/python3
"""
Lists all State objects
from the database hbtn_0e_6_usa.
"""

from sys import argv
from model_city import City, Base
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Database access

    """

    db = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    engine = create_engine(db)
    Session = sessionmaker(bind=engine)

    session = Session()

    results = session.query(City, State).join(State)
    for city, state in results.all():
        print('{}: ({}) {}'.format(state.name, city.id, city.name))
    session.commit()
    session.close()
