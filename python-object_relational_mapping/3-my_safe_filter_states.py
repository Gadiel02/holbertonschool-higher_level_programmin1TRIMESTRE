#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Get the arguments from the command line
    if len(sys.argv) != 5:
        print("Usage: ./3-my_safe_filter_states.py <mysql username> <mysql password> <database name> <state name searched>")
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name_searched = sys.argv[4]

    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Prepare a parameterized query to prevent SQL injection
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name_searched,))

    # Fetch all the results of the executed query
    results = cursor.fetchall()

    # Print each result
    for row in results:
        print(row)

    # Close the cursor and the database connection
    cursor.close()
    db.close()
