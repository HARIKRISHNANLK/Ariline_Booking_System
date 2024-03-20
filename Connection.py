import mysql
import mysql.connector as sql

class fetch:
    host = "localhost"
    user = "root"
    password ="root"
    db = "airlines_booking"


class connection:
        conn = mysql.connector.connect(host=fetch.host, user=fetch.user, password=fetch.password,
                                       database=fetch.db)
        my_cursor = conn.cursor()
        # A cursor is an object which helps to execute the query and fetch the records from the database.
        print("Welcome")

#doing connection part in this module
