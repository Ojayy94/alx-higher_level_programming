#!/usr/bin/python3
"""A script that lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys


if __name__ == '__main__':
    """our script should take 3 arguments: mysql username, mysql
    password and database name (no argument validation needed)

    You must use the module MySQLdb (import MySQLdb)

    Your script should connect to a MySQL server running on
    localhost at port 3306

    Results must be sorted in ascending order by states.id
    """

    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    script = db.cursor()
    script.execute(`SELECT * FROM states`)
    show = script.fetchall()

    for i in show:
        print(i)
