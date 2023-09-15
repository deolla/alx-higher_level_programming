#!/usr/bin/python3
import MySQLdb

db = MySQLdb.connect(host="localhost", port=3306, user="username", passwd="password", db="database_name")
cur = db.cursor()
cur.execute("SELECT * FROM states ORDER BY states.id")
states = cur.fetchall()
for state in states:
    print(state)
cur.close()
db.close()
