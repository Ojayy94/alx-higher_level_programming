#!/usr/bin/python3
"""A script that lists all cities from the database hbtn_0e_0_usa"""

import MySQLdb
from sys import argv


if __name__ == '__main__':
    """our script should take 3 arguments: mysql username, mysql
    password and database name (no argument validation needed)

    You must use the module MySQLdb (import MySQLdb)

    Your script should connect to a MySQL server running on
    localhost at port 3306

    Results must be sorted in ascending order by cities.id
    """

    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    script = db.cursor()
    script.execute("SELECT * FROM cities \
                 INNER JOIN states \
                 ON cities.state_id = states.id \
                 ORDER BY cities.id ASC")
    show = script.fetchall()

    if shows is not None:
        print(", ".join([show[1] for shows in show]))
