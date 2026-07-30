#!/usr/bin/python3
"""Lists all the cities of a database with the name of their state."""
import sys
import MySQLdb


if __name__ == "__main__":
    database = MySQLdb.connect(host="localhost", port=3306,
                               user=sys.argv[1], passwd=sys.argv[2],
                               db=sys.argv[3])
    cursor = database.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities"
                   " JOIN states ON cities.state_id = states.id"
                   " ORDER BY cities.id ASC")
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    database.close()
