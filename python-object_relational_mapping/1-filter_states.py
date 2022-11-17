#!/usr/bin/python3
"""
Write a script that lists all states with a name
starting with N (upper N) from
the database hbtn_0e_0_usa:
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

    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' \
            ORDER BY states.id ASC")

    rows = cursor.fetchall()
    for col in rows:
        print(col)

    db.close()


if __name__ == "__main__":
    mysqlconnect()
