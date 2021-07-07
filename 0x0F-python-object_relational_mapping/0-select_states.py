#!/usr/bin/python3
"""Lists all states from the database
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', argv[1], argv[2], argv[3], port=3306)
    position = db.cursor()
    position.execute("SELECT * FROM states")
    row = position.fetchall()
    for item in row:
        print(item)
