-- script that lists all records of the table second_table of the database 
mysql> SELECT score, name FROM second_table WHERE name != '' OR IS NOT NULL ORDER BY score DESC;