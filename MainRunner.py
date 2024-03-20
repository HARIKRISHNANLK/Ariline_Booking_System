import mysql.connector
import Main.Connection
import Main.User
import Main.Searchflight
import Main.PassangerDetails
import Main.Booking
import Main.payment
import subprocess

subprocess.call("Searchflight.py", shell=True)
# Use the subprocess Module to Run a Python Script in Another Python Script
import Main.CancellationandRefund
import Main.regex
import re
from Main.Connection import connection

connection.my_cursor.close()