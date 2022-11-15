#!/usr/bin/python3
import MySQLdb
""" Write a script that lists all states from the database hbtn_0e_0_usa:  """

""" Function for connecting to MySQL database"""
def mysqlconnect():

    """Open database connection """ 
    db = MySQLdb.connect(
        host="localhost",
        user="root",
        password='',
        database="hbtn_0e_0_usa",
        port=3306
        )
               
    cursor = db.cursor()

    sql = "SELECT * FROM states ORDER BY states.id ASC"
    """Create table as per requirement"""
 
    cursor.execute(sql)

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    db.close()
    """disconnect from server"""
 
""" Function Call For Connecting To Our Database"""
mysqlconnect()