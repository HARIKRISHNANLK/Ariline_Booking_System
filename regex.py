import mysql.connector
import Main.Connection
import Main.User
import re



def check(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    # pass the regular expression
    # and the string into the fullmatch() method
    if (re.fullmatch(regex, email)):
        pass
    else:
        print("Invalid Email")
        breakpoint()

def checkname(name):
    # pass the regular expression
    # and the string into the fullmatch() method
    regexname = re.compile('[A-Za-z]{2,25}( [A-Za-z]{2,25})?')
    if regexname.findall(name):
        pass
    else:
        print("INVALID USERNAME")
        breakpoint()

def checknum(phno):
    # pass the regular expression
    # and the string into the fullmatch() method
    reg = re.compile(r"[\d]{3}[\d]{3}[\d]{3}")
    if reg.findall(phno):
        pass
    else:
        print("INVALID PHONE NUMBER")
        breakpoint()

def checkcity(city):
    # pass the regular expression
    # and the string into the fullmatch() method
    reg = re.compile("^([a-zA-Z\u0080-\u024F]+(?:. |-| |'))*[a-zA-Z\u0080-\u024F]*$")
    if reg.findall(city):
        pass
    else:
        print("INVALID NAME")
        breakpoint()

def checkpass(passwd):
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$"

    # compiling regex
    match_re = re.compile(reg)

    # searching regex
    res = re.search(match_re, passwd)

    # validating conditions
    if res:
        pass
    else:
        print("Invalid Password")

def checkage(age):
    # pass the regular expression
    # and the string into the fullmatch() method
    if(age>=1 and age<=99):
        pass
    else:
        print("INVALID AGE")
        breakpoint()
def checkage1(age):
    # pass the regular expression
    # and the string into the fullmatch() method
    while(True):
        if (age >= 1 and age <= 99):
            break