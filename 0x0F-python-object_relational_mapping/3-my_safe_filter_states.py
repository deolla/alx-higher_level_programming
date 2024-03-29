#!/usr/bin/python3
"""
Write a script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
     host="localhost",
     user=sys.argv[1],
     passwd=sys.argv[2],
     db=sys.argv[3],
     port=3306
    )
    state_name = sys.argv[4]
    cur = db.cursor()
    m = "SELECT * FROM states WHERE name LIKE BINARY %s"
    cur.execute(m, (state_name,))
    states = cur.fetchall()
    for i in states:
        print(i)
    cur.close()
    db.close()
