# cancellation and refund
import mysql

import Main.Connection
import Main.Searchflight

import logging
logging.basicConfig(
     filename="log.txt",
     level=logging.INFO,
     format= '[%(asctime)s] %(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
     datefmt='%H:%M:%S'
 )


#create a  function of cancel ticket
mm = Main.Connection.connection.my_cursor
def cancel_ticket():
    logging.info("Cancel the ticket")

    try:


# passanger name,passenger id
        name = (input("\nEnter the Passanger_Name :- "))
        # Entering the passanger name
        query16 = (f"select count(*) from passenger where name='{name}'")
        mm.execute(query16)
        s = mm.fetchone()
        # fetchone returns next row of a query result set
        if (s[0] == 1):
            pass
        else:
            print("Please Enter proper Passanger Name")
            breakpoint()
        # taking an input from user and checking the name with the database.


        passenger_id = (int(input("\nEnter the Passenger id :- ")))
        query17 = (f"select count(*) from passenger where passenger_id='{passenger_id}'")
        mm.execute(query17)
        # executing query17
        s = mm.fetchone()
        # fetchone returns next row of a query result set
        if (s[0] == 1):
            pass
        else:
            print("Please Enter proper PassangerId")
            breakpoint()
        # taking an input from user and checking the name with the database.

        query1 = "DELETE  FROM passenger WHERE passenger_id='{}' and name='{}'".format(passenger_id,name)
        # query for deleting the data from the database
        c = Main.Connection.connection.my_cursor
        # initializing the cursor
        c.execute(query1)
        # executing the query1
        Main.Connection.connection.conn.commit()
        # This method sends a COMMIT statement to the MySQL server,
        # committing the current transaction.
        # Since by default Connector/Python does not autocommit, it is important to call this method -
        # after every transaction that modifies data for tables that use transactional storage engines.
        print("\n YOUR BOOKING SUCCESSFULLY CANCELLED.\nSEE YOU NEXT TIME.\n\n THANK YOU")
        exit()
    except mysql.connector.Error as e:
            logging.error("Error reading data from MySQL table", e)