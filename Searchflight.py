# flight number,mannualy,cancellation

import Main.Connection
import mysql

import Main.Connection
import Main.CancellationandRefund
import logging

logging.basicConfig(
    filename="log.txt",
    level=logging.INFO,
    format='[%(asctime)s] %(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)

# search your flight
mm = Main.Connection.connection.my_cursor  # enabling the cursor for sql operation

print("\nChoose one of the options below")
print("1.flight number")
print("2.mannualy")
print("3.cancellation and refund")
print("4.exit")
# taking input from the user

ans = int(input("\nAnswer (1/2/3/4):-"))
try:
    logging.info("Searching flight using flight number")

    if ans == 4:
        exit()
    # if the ans is 4 it will exit the program

    if ans == 1:
        num = (input("\nENTER FLIGHT NUMBER:-(Ex: SG773)"))
        query13 = (f"select count(*) from flights where FLIGHT_NO='{num}'")
        mm.execute(query13)
        s = mm.fetchone()  # variable storing fetched database as tuple
        if (s[0] == 1):
            pass
        else:
            print("Invalid flight number")
            breakpoint()
        # When user gives a flight number as input, it will check whether the perticular flight exists in the database
        # It returns the details , then it will go to the next step, else it will show invalid flight number
        query = "SELECT AIRLINES_NAME, DEPARTURE, DESTINATION, FLIGHT_NO,TIME_OF_DEPARTURE, TIME_OF_ARRIVAL,CHARGES FROM FLIGHTS WHERE FLIGHT_NO = '{}' ".format(
            num)
        Main.Connection.connection.my_cursor.execute(query)
        print("\nYOUR FLIGHT DATA IS")
        for a in Main.Connection.connection.my_cursor:
            print("AIRLINES_NAME, DEPARTURE, DESTINATION, FLIGHT_NO, TIME_OF_DEPARTURE, TIME_OF_ARRIVAL, CHARGES")
            print(a)  # shows the complete the data of selected flight
except mysql.connector.Error as e:
    logging.error("Error reading data from MySQL table", e)

# creating empty list to append the input data

departurelocation = []  # creating empty list to store departure location
arrivallocation = []  # creating empty list to store arrival location
fliname = []  # empty list to store flight name


def flight_data():
    try:
        logging.info("fetching flight data")

        departure = input("\nENTER YOUR DEPARTURE LOCAION:-")
        query14 = (f"select count(*) from flights where DEPARTURE='{departure}'")
        arrival = input("\nENTER YOUR ARRIVAL LOCATION:-")

        query15 = (f"select count(*) from flights where DESTINATION='{arrival}'")
        query2 = "SELECT AIRLINES_NAME FROM FLIGHTS WHERE DEPARTURE = '{}' AND DESTINATION = '{}'".format(departure,
                                                                                                          arrival)
        departurelocation.append(departure)
        arrivallocation.append(arrival)
        Main.Connection.connection.my_cursor.execute(query2)
        print("\nYOUR REQUIRED FLIGHTS ARE------")
        for b in Main.Connection.connection.my_cursor:
            print(b)  # shows the complete the data of available flight
        fly = input("\nENTER A FLIGHT NAME YOU WANT:-")
        fliname.append(fly)
        print("\nHEAR THE DETAILS OF YOUR FLIGHT--")
        print("AIRLINES_NAME, DEPARTURE, DESTINATION, FLIGHT_NO, TIME_OF_DEPARTURE, TIME_OF_ARRIVAL, CHARGES")
        query3 = "SELECT AIRLINES_NAME, DEPARTURE, DESTINATION, FLIGHT_NO,TIME_OF_DEPARTURE, TIME_OF_ARRIVAL,CHARGES FROM FLIGHTS WHERE AIRLINES_NAME = '{}' AND DEPARTURE = '{}' AND DESTINATION = '{}' ".format(
            fly,
            departure,
            arrival)
        # showing the details of flight with respect to the given data
        Main.Connection.connection.my_cursor.execute(query3)
        # executing query3
        for c in Main.Connection.connection.my_cursor:
            return print(c)  # shows the complete the data of selected flight

    except mysql.connector.Error as h:
        logging.error("Error reading data from MySQL table", h)


if ans == 2:
    flight_data()  # calling the function flight data

con = input("\nWould you like to continue with Ticket Booking (Y/N):-")
while True:
    if con == 'n' or con == 'N' or con == 'no' or con == 'NO':
        print("****Thank you****")
        exit()
    else:
        break

if ans == 3:
    Main.CancellationandRefund.cancel_ticket()

    # calling the function cancellation from Cancellation and refund module