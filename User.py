import mysql.connector
import re
import Main.Connection
import Main.regex
import logging

logging.basicConfig(
     filename="log.txt",
     level=logging.INFO,
     format= '[%(asctime)s] %(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
     datefmt='%H:%M:%S'
 )

#importing all the required modules to run this  user part

print("\n********************WELCOME TO FLIGHT BOOKING SYSTEM***********************")

acc = input("\nDO YOU HAVE AN ACCOUNT (Y/N)")


fullname = []
phno = []
cityname = []
statename = []
useremail = []
passwd = []
# Creating empty list to store the input data

mm = Main.Connection.connection.my_cursor #mm -> cursor name
if acc == 'n' or acc == 'N' or acc == 'no' or acc == 'NO' :
    try:
        logging.info("fetching flight data")

        name = input("\nENTER YOUR FULL NAME:-")
        Main.regex.checkname(name)
        #Calling checkname function for validating the input data
        fullname.append(name)
        #appending the data into fullname list
        ph = (input("\nENTER YOUR PHONE NO:-"))
        Main.regex.checknum(ph)
        # Calling checknum function for validating the input data
        phno.append(ph)
        # appending the data into phno list
        city = input("\nENTER YOUR CITY NAME:-")
        Main.regex.checkcity(city)
        cityname.append(city)
        # Calling the function checkcity for validation and appending the data into cityname
        state = input("\nENTER YOUR STATE:-")
        Main.regex.checkcity(state)
        statename.append(state)
        # Calling the function checkstate for validation and appending the data into statename
        email = input("\nENTER YOUR EMAIL ID:-")
        Main.regex.check(email)
        useremail.append(email)
        # Calling the function check for validation and appending the data into useremail
        passw = input("\nENTER YOUR PASSWORD:- should be \n One Capital Letter\n Special Character\n One Number \n Length Should be 8-18\n")
        Main.regex.checkpass(passw)
        passwd.append(passw)
        # Calling the function checkpass for validation and appending the data into password


        sql = "insert into user(name,phonenumber,city,state,email,password)values(%s,%s,%s,%s,%s,%s)"
        record = (name, ph, city, state, email, passw)
        # record is a tuple file which is storing the data for execution

        mm.execute(sql, record)
        # execute the statement using the query and record

        Main.Connection.connection.conn.commit()

        #inserting all the input data into sql database
        print("\n-------YOUR ACCOUNT IS CREATED SUCCESSFULLY-------")
    except mysql.connector.Error as h:
        logging.error("Error reading data from MySQL table", h)

elif acc == 'y' or acc == 'yes' or acc == 'Y' or acc == 'YES':

        emaillogin = input("\nENTER YOUR EMAIL ID:-")
        #taking email  input from user

        query12=(f"select count(*) from user where email='{emaillogin}'")
        mm.execute(query12)
        s=mm.fetchone()
        if(s[0] == 1):
            pass
        else:
            print("Invalid Email")
            breakpoint()

        paswordlogin = input("\nENTER YOUR PASSWORD:-")
        query13 = (f"select count(*) from user where password='{paswordlogin}'")
        mm.execute(query13)
        s = mm.fetchone()
        # variable storing all the fetched data
        # fetchone returns a query result set
        if (s[0] == 1):
            print("login successful")
        else:
            print("Invalidpassword")
            exit()

else:
    print("PLEASE TYPE YES OR NO")
    exit()
