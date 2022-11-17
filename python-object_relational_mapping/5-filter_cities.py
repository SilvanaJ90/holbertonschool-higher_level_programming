#!/usr/bin/python3
"""
Write a script that lists
all cities from the database hbtn_0e_4_usa
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

    cursor.execute("SELECT C.name \
            FROM cities C \
            LEFT JOIN states S \
            ON S.id = C.state_id; \
            WHERE S.name = LIKE BINARY %s \
            ORDER BY C.id ASC",(argv[4],))

    rows = cursor.fetchall()
    cont = 0
    lista = []
    for col in rows:
        lista.append(col[0])
    print(", ".join(lista))
    db.close()


if __name__ == "__main__":
    mysqlconnect()
