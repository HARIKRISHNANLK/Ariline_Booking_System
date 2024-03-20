import mysql.connector
import Main.Connection
import Main.Searchflight
import Main.PassangerDetails
import logging
logging.basicConfig(
     filename="log.txt",
     level=logging.INFO,
     format= '[%(asctime)s] %(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
     datefmt='%H:%M:%S'
 )
#importing required modules to run this class


flo = [] # Variable storing flight number
tdep = [] # Variable storing time of departure
tarr = [] # Variable storing time of arrival


def fl_nm():
    try:
        logging.info("started")
        query4 = "SELECT FLIGHT_NO FROM FLIGHTS WHERE airlines_name = '{}' and DEPARTURE = '{}' and DESTINATION = '{}' ".format(
            Main.Searchflight.fliname[0], Main.Searchflight.departurelocation[0], Main.Searchflight.arrivallocation[0])
        Main.Connection.connection.my_cursor.execute(query4)
        for f in Main.Connection.connection.my_cursor:
            flo.append(f)
        # Executing the query for selecting flight number with respect to the given airlines name, departure location and destination location.
        # Appending the variable into flo(list storing flight number)


        query5 = "SELECT TIME_OF_DEPARTURE FROM FLIGHTS WHERE airlines_name = '{}' and DEPARTURE = '{}' and DESTINATION = '{}' ".format(
            Main.Searchflight.fliname[0], Main.Searchflight.departurelocation[0], Main.Searchflight.arrivallocation[0])
        Main.Connection.connection.my_cursor.execute(query5)
        for g in Main.Connection.connection.my_cursor:
            tdep.append(g)
            # Executing the query for selecting time of departure with respect to the given airlines name, departure location and destination location.
            # Appending the variable into tdep(list storing time of departure)

        query6 = "SELECT TIME_OF_ARRIVAL FROM FLIGHTS WHERE airlines_name = '{}' and DEPARTURE = '{}' and DESTINATION = '{}' ".format(
        Main.Searchflight.fliname[0], Main.Searchflight.departurelocation[0], Main.Searchflight.arrivallocation[0])
        Main.Connection.connection.my_cursor.execute(query6)
        for h in Main.Connection.connection.my_cursor:
            tarr.append(h)
            # Executing the query for selecting time of arrival with respect to the given airlines name, departure location and destination location.
            # Appending the variable into tarr(list storing time of arrival)
    except mysql.connector.Error as e:
        logging.error("Error reading data from MySQL table", e)


an = [] #Variable storing the flight name
de = [] # Variable storing the departure location
ds = [] # Variable storing the destination location
td = [] # Variable storing time of departure
ta = [] # variable storing time of arrival


def fl_no():
    try:
        logging.info("started")

        query7 = "SELECT AIRLINES_NAME FROM FLIGHTS  WHERE FLIGHT_NO = '{}'".format(Main.Searchflight.num)
        Main.Connection.connection.my_cursor.execute(query7)
        for i in Main.Connection.connection.my_cursor:
            an.append(i)
        # Executing the query for selecting Airline name with the given flight number.
        # Appending the variable into an(list storing flight name)

        query8 = "SELECT DEPARTURE FROM FLIGHTS WHERE FLIGHT_NO = '{}'".format(Main.Searchflight.num)
        Main.Connection.connection.my_cursor.execute(query8)
        for j in Main.Connection.connection.my_cursor:
            de.append(j)
        # Executing the query for selecting Departure location with the given flight number.
        # Appending the variable into de(list storing departure location)

        query9 = "SELECT DESTINATION FROM FLIGHTS WHERE FLIGHT_NO = '{}'".format(Main.Searchflight.num)
        Main.Connection.connection.my_cursor.execute(query9)
        for k in Main.Connection.connection.my_cursor:
            ds.append(k)
        # Executing the query for selecting Destination location with the given flight number.
        # Appending the variable into ds(list storing destination location)

        query10 = "SELECT TIME_OF_DEPARTURE FROM FLIGHTS WHERE FLIGHT_NO = '{}'".format(Main.Searchflight.num)
        Main.Connection.connection.my_cursor.execute(query10)
        for l in Main.Connection.connection.my_cursor:
            td.append(l)
        # Executing the query for selecting time of departure with the given flight number.
        # Appending the variable into td(list storing time of departure)

        query11 = "SELECT TIME_OF_ARRIVAL FROM FLIGHTS WHERE FLIGHT_NO = '{}'".format(Main.Searchflight.num)
        Main.Connection.connection.my_cursor.execute(query11)
        for m in Main.Connection.connection.my_cursor:
            ta.append(m)
        # Executing the query for selecting time of arrival with the given flight number.
        # Appending the variable into ta(list storing time of arrival)
    except mysql.connector.Error as e:
        logging.error("Error reading data from MySQL table", e)


payment = []
#creating an empty list to append payment value
try:
    logging.info("started")

    if Main.Searchflight.ans == 1 and Main.PassangerDetails.cl == 1:
            fl_no()
            query12 = "SELECT CHARGES*{} FROM FLIGHTS WHERE FLIGHT_NO = '{}'".format(Main.PassangerDetails.passenger, Main.Searchflight.num)
            Main.Connection.connection.my_cursor.execute(query12)
            #calculating the charges with respect to the selected class
            print(f"\nnames = {Main.PassangerDetails.nameofpassanger}               age = {Main.PassangerDetails.ageofpassanger}           gender = {Main.PassangerDetails.genderofpassanger}")
            print(f"flight name = {an}         departure = {de}       destination = {ds}")
            print(f"flight number = {Main.Searchflight.num}      diparture time = {td}        arrival time = {ta}     ")
            print("class = economy class")
            #displaying the details given by the user which we stored in the lists
            for n in Main.Connection.connection.my_cursor:
                payment.append(n)
                # Total payment value will show with respect to the number of passenger
                print(f"\nYOU HAVE TO PAY {n} RUPEES")

    elif Main.Searchflight.ans == 1 and Main.PassangerDetails.cl == 2:
            fl_no()
            query13 = "SELECT (CHARGES +CHARGES*0.2)*{} FROM FLIGHTS WHERE flight_no = '{}' ".format(Main.PassangerDetails.passenger, Main.Searchflight.num)
            Main.Connection.connection.my_cursor.execute(query13)
            print(f"\nnames = {Main.PassangerDetails.nameofpassanger}               age = {Main.PassangerDetails.ageofpassanger}           gender = {Main.PassangerDetails.genderofpassanger}")
            print(f"flight name = {an}         departure = {de}       destination = {ds}")
            print(f"flight number = {Main.Searchflight.num}      diparture time = {td}        arrival time = {ta}     ")
            print("class = business class")
            # displaying the details given by the user which we stored in the lists
            for o in Main.Connection.connection.my_cursor:
                payment.append(o)
                # Total payment value will show with respect to the number of passenger
                print(f"\nYOU HAVE TO PAY {o} RUPEES")

    elif Main.Searchflight.ans == 1 and Main.PassangerDetails.cl == 3:
            fl_no()
            query14 = "SELECT (CHARGES +CHARGES*0.4)*{} FROM FLIGHTS WHERE FLIGHT_NO = '{}'".format(Main.PassangerDetails.passenger, Main.Searchflight.num)
            Main.Connection.connection.my_cursor.execute(query14)
            print(f"\nnames = {Main.PassangerDetails.nameofpassanger}               age = {Main.PassangerDetails.ageofpassanger}           gender = {Main.PassangerDetails.genderofpassanger}")
            print(f"flight name = {an}         departure = {de}       destination = {de}")
            print(f"flight number = {Main.Searchflight.num}      diparture time = {td}        arrival time = {ta}     ")
            print("class = first class")
            # displaying the details given by the user which we stored in the lists
            #Since some variable using here got declared in another python module, we have to give the path for the varable
            for p in Main.Connection.connection.my_cursor:
                payment.append(p)
                # Total payment value will show with respect to the number of passenger
                print(f"\nYOU HAVE TO PAY {p} RUPEES")


    elif Main.Searchflight.ans == 2 and Main.PassangerDetails.cl == 1:
            fl_nm()
            query15 = "SELECT CHARGES*{} FROM FLIGHTS WHERE airlines_name = '{}' and DEPARTURE = '{}' and DESTINATION = '{}' ".format(
                Main.PassangerDetails.passenger, Main.Searchflight.fliname[0], Main.Searchflight.departurelocation[0], Main.Searchflight.arrivallocation[0])
            Main.Connection.connection.my_cursor.execute(query15)
            print(f"\nnames = {Main.PassangerDetails.nameofpassanger}               age = {Main.PassangerDetails.ageofpassanger}           gender = {Main.PassangerDetails.genderofpassanger}")
            print(f"flight name = {Main.Searchflight.fliname}         departure = {Main.Searchflight.departurelocation}       destination = {Main.Searchflight.arrivallocation}")
            print(f"flight number = {flo}      diparture time = {tdep}        arrival time = {tarr}     ")
            print("class = economy class")
            # displaying the details given by the user which we stored in the lists
            # Since some variable using here got declared in another python module, we have to give the path for the varable
            for q in Main.Connection.connection.my_cursor:
                payment.append(q)
                # Total payment value will show with respect to the number of passenger
                print(f"\nYOU HAVE TO PAY {q} RUPEES")

    elif Main.Searchflight.ans == 2 and Main.PassangerDetails.cl == 2:
            fl_nm()
            query16 = "SELECT (CHARGES +CHARGES*0.2)*{} FROM FLIGHTS WHERE airlines_name = '{}' and DEPARTURE = '{}' and DESTINATION = '{}' ".format(
                Main.PassangerDetails.passenger, Main.Searchflight.fliname[0], Main.Searchflight.departurelocation[0], Main.Searchflight.arrivallocation[0])
            Main.Connection.connection.my_cursor.execute(query16)
            print(f"\nnames = {Main.PassangerDetails.nameofpassanger}               age = {Main.PassangerDetails.ageofpassanger}           gender = {Main.PassangerDetails.genderofpassanger}")
            print(f"flight name = {Main.Searchflight.fliname}         departure = {Main.Searchflight.departurelocation}       destinatio = {Main.Searchflight.arrivallocation}")
            print(f"flight number = {flo}      diparture time = {tdep}        arrival time = {tarr}     ")
            print("class = business class")
            # displaying the details given by the user which we stored in the lists
            # Since some variable using here got declared in another python module, we have to give the path for the varable
            for r in Main.Connection.connection.my_cursor:
                payment.append(r)
                # Total payment value will show with respect to the number of passenger
                print(f"\nYOU HAVE TO PAY {r} RUPEES")

    elif Main.Searchflight.ans == 2 and Main.PassangerDetails.cl == 3:
            fl_nm()
            query17 = "SELECT (CHARGES +CHARGES*0.4)*{} FROM FLIGHTS WHERE airlines_name = '{}' and DEPARTURE = '{}' and DESTINATION = '{}' ".format(
                Main.PassangerDetails.passenger, Main.Searchflight.departurelocation[0], Main.Searchflight.departurelocation[0], Main.Searchflight.arrivallocation[0])
            Main.Connection.connection.my_cursor.execute(query17)
            print(f"\nnames = {Main.PassangerDetails.nameofpassanger}               age = {Main.PassangerDetails.ageofpassanger}           gender = {Main.PassangerDetails.genderofpassanger}")
            print(f"flight name = {Main.Searchflight.fliname}         departure = {Main.Searchflight.departurelocation}       destination = {Main.Searchflight.arrivallocation}")
            print(f"flight number = {flo}      diparture time = {tdep}        arrival time = {tarr}     ")
            print("class = first class")
            # displaying the details given by the user which we stored in the lists
            # Since some variable using here got declared in another python module, we have to give the path for the varable
            for s in Main.Connection.connection.my_cursor:
                payment.append(s)
            # Total payment value will show with respect to the number of passenger
                print(f"\nYOU HAVE TO PAY {s} RUPEES")
except mysql.connector.Error as e:
    logging.error("Error reading data from MySQL table", e)
