#!/usr/bin/python3
import MySQLdb
""" Write a script that lists all states from the database hbtn_0e_0_usa:  """
 
"""Open database connection """ 
db = MySQLdb.connect(host="localhost",user="root",password='',database="hbtn_0e_0_usa",port=3306)
 
cursor = db.cursor()
 
"""Create table as per requirement"""
sql = "SELECT * FROM states ORDER BY states.id ASC"
 
cursor.execute(sql) #table created
 
"""disconnect from server"""
db.close()