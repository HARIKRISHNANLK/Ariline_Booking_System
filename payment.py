

import mysql
import mysql.connector as sql
import Main.Connection
import logging
logging.basicConfig(
     filename="log.txt",
     level=logging.INFO,
     format= '[%(asctime)s] %(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
     datefmt='%H:%M:%S'
 )



pay = input("\nTO PAY PRESS (P):-")
# creating a function for payment
def pay():

    try:
        logging.info("payment started")

        print("\nHOW YOU WANT TO PAY ?")
        print("1.GOOGLE PAY")
        print("2.AMAZON PAY")
        print("3.PAYPAL")
        print("4.APPLE PAY")
        print("5.CREDIT CARD")
        print("6.DEBIT CARD")
        #asking customer the way to make their payment


        pay2 = int(input("\nENTER YOUR PAYMENT METHOD (1/2/3/4/5/6):-"))
        # pay2 is an intiger type variable storing the input from user


        if pay2 == 1:
            print("\n-------------------GOOGLE PAY---------------------------")
            int(input("Enter your google pay number"))
            pay3 = input("\nTO CONTINUE PAYMENT PRESS (P):-")
            print("\nTRANSACTION SUCCESSFUL------------")

        elif pay2 == 2:
            print("\n-------------------AMAZON PAY---------------------------")
            print(F"PAY  RUPEES")
            pay3 = input("\nTO CONTINUE PAYMENT PRESS (P):-")
            print("\nTRANSACTION SUCCESSFUL------------")

        elif pay2 == 3:
            print("\n-------------------PAYPAL---------------------------")
            print(F"PAY  RUPEES")
            pay3 = input("\nTO CONTINUE PAYMENT PRESS (P):-")
            print("\nTRANSACTION SUCCESSFUL------------")

        elif pay2 == 4:
            print("\n-------------------APPLE PAY---------------------------")
            print(F"PAY  RUPEES")
            pay3 = input("\nTO CONTINUE PAYMENT PRESS (P):-")
            print("\nTRANSACTION SUCCESSFUL------------")

        elif pay2 == 5 or pay2 == 6:
            print("\n-------------------CARD payment---------------------------")
            print(F"PAY  RUPEES")
            c_no = int(input("\nENTER YOUR CARD NO:-"))
            cvv = int(input("\nENTER YOUR CVV:-"))
            print("\nTRANSACTION SUCCESSFUL------------")
        else:
            print("Print a valid number")
            exit()

    except ValueError:
        print("Please enter a valid number")
    except mysql.connector.Error as e:
        logging.error("Error reading data from MySQL table", e)

pay() # calling pay function
print(f"\nYOUR TICKETS ARE SEND TO YOUR EMAIL ")
print("\n--------THANKS FOR USING FLIGHT BOOKING SYSTEM--------------")