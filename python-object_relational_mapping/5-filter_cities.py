#!/usr/bin/python3
"""Lists all the cities of a state given as argument."""
import sys
import MySQLdb


if __name__ == "__main__":
    database = MySQLdb.connect(host="localhost", port=3306,
                               user=sys.argv[1], passwd=sys.argv[2],
                               db=sys.argv[3])
    cursor = database.cursor()
    cursor.execute("SELECT cities.name FROM cities"
                   " JOIN states ON cities.state_id = states.id"
                   " WHERE states.name = %s"
                   " ORDER BY cities.id ASC", (sys.argv[4],))
    print(", ".join(row[0] for row in cursor.fetchall()))
    cursor.close()
    database.close()
