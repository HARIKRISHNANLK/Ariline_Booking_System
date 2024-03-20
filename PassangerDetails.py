import Main.Connection
import Main.regex
import logging
import mysql

logging.basicConfig(
     filename="log.txt",
     level=logging.INFO,
     format= '[%(asctime)s] %(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
     datefmt='%H:%M:%S'
 )
# doing the logging part

print("\nCHOOSE THE CLASS OF TRAVEL:-")
print("1.ECONOMY CLASS")
print("2.BUSINESS CLASS (+20% CHARGES)")
print("3.FIRST CLASS (+40% CHARGES)")

cl = int(input("\nENTER CLASS NO (1/2/3):-"))


passenger = int(input("\nENTER THE NUMBER OF PASSANGERS:-")) #number of passengers is storing in variable passanger

nameofpassanger = []
ageofpassanger = []
genderofpassanger = []
passangerid = []
# creating three empty list nameofpassanger ageofpassanger genderofpassanger for storing the passanger data.
# we will display the data before payment

def pass_data():
#creating a funtion pass_data where we taking the input data from passanger storing in database
    try:
        logging.info("Taking input from passanger")
        name = input("\nENTER THE NAME OF A PASSENGER:-")
        Main.regex.checkname(name)
        age =int(input(f"\nENTER THE AGE OF {name}:-"))
        Main.regex.checkage(age)
        gender = input("\nGENDER:-")
        #As there are so many genders existing in world we are not giving a specific validation for gender

        nameofpassanger.append(name)
        ageofpassanger.append(age)
        genderofpassanger.append(gender)
        # appending all the input datas into list above declared
        m =  Main.Connection.connection.my_cursor #initializing cursor
        sql = "insert into Passenger(name,age,gender)values(%s,%s,%s)"
        record = (name, age, gender)
        #record is a tuple file which is storing the data for execution
        m.execute(sql, record)
        # execute the statement using the query and record
        Main.Connection.connection.conn.commit()
        # This method sends a COMMIT statement to the MySQL server,
        # committing the current transaction.
        # Since by default Connector/Python does not autocommit, it is important to call this method -
        # after every transaction that modifies data for tables that use transactional storage engines.
        print("\n-------DATA ENTERED SUCCESSFULLY-------")

    except mysql.connector.Error as e:
        logging.error("Error reading data from MySQL table", e)



for d in range(passenger):
    pass_data()
# calling the function passenger  number of times
# passanger is the int type variable we declared above to store number of passenger


ch = input("\nWould you like to continue with Ticket Booking (Y/N):-")
#asking customer whether they want to add more passengers or not

while True:
    if ch == 'n' or ch == 'N' or ch == 'no' or ch == 'NO':
        # ch refers to the user opinion whether the user has to continue this operation or not.
        for e in range(passenger):
            pass_data()
        querycall = ("select * from passenger")
        Main.Connection.connection.my_cursor.execute(querycall)
    else:
        break

