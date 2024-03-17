#!/usr/bin/python3
"""A script that lists all states from the database hbtn_0e_0_usa"""

from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == '__main__':
    """our script should take 3 arguments: mysql username, mysql
    password and database name (no argument validation needed)

    You must use the module MySQLdb (import MySQLdb)

    Your script should connect to a MySQL server running on
    localhost at port 3306

    Results must be sorted in ascending order by states.id
    """

    db = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                       .format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=db)
    session = Session()

    query = session.query(City, State).join(State)

    for city, state in query.all():
        print("{}: ({:d}) {}".format(state.name, city.id, city.name))
    session.commit()
    session.close()
