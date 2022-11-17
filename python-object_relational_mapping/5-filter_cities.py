#!/usr/bin/python3
"""
Write a script that takes in the name of
a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv


def mysqlconnect():
    """ Function for connecting to MySQL database"""
    db = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        password='',
        database=argv[3],
        port=3306
        )

    cursor = db.cursor()

    sql = "SELECT * FROM states WHERE name = BINARY '{}' \
             ORDER BY states.id ASC".format(argv[4])

    cursor.execute(sql)

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    db.close()


if __name__ == "__main__":
    mysqlconnect()