#!/usr/bin/python3
import MySQLdb
""" Write a script that lists all states from the database hbtn_0e_0_usa:  """
 

db = MySQLdb.connect(host="localhost",user="root",password='',database="hbtn_0e_0_usa",port=3306)
"""Open database connection """ 
 
cursor = db.cursor()

sql = "SELECT * FROM states ORDER BY states.id ASC"
"""Create table as per requirement"""
 
cursor.execute(sql) #table created

db.close()
"""disconnect from server"""