#!/usr/bin/python3
"""
Lists all states from the database
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', argv[1], argv[2], argv[3])
    position = db.cursor()
    position.execute("SELECT * FROM states")
    row = position.fetchall()
    for item in row:
        print(item)