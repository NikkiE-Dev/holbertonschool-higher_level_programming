#!/usr/bin/python3
"""Lists all states starting with N from the db
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', argv[1], argv[2], argv[3], port=3306)
    pos = db.cursor()
    rows = pos.execute(SELECT * FROM states WHERE states.name LIKE '%N' ORDER BY states.id)
    get_row = pos.fetchall()
    for row in get_row:
        print(row)
