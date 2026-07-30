#!/usr/bin/python3
"""Safely lists the states of a database whose name matches an argument."""
import sys
import MySQLdb


if __name__ == "__main__":
    database = MySQLdb.connect(host="localhost", port=3306,
                               user=sys.argv[1], passwd=sys.argv[2],
                               db=sys.argv[3])
    cursor = database.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY %s"
                   " ORDER BY states.id ASC", (sys.argv[4],))
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    database.close()
