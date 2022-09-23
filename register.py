from login import login
import re
import os
path = os.path.dirname(os.path.abspath(__file__))


EMAIL_REG = re.compile(
    r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9]+(\.[A-Z|a-z]{2,})+')
PHONE_REG = re.compile(r'^01[0-2,5]{1}[0-9]{8}$')
user = {
    "fname": "",
    "lname": "",
    "email": "",
    "password": "",
    "phone": ""
}


def register():
    print("------------registeration forum----------- :\n")
    user["fname"] = getname()
    user["lname"] = getlastname()
    user["phone"] = getnumber()
    while not is_valid_phone(user["phone"]):
        print("please use a valid phone no!")
        user["phone"] = getnumber()
    user["email"] = getmail()
    while not is_valid_email(user["email"]):
        print("please use a valid mail!")
        user["email"] = getmail()
    user["password"] = getpassword()
    while not passwordmatch((user["password"]), getpasswordagain()):
        print(" passwords must match!")
        user["password"] = getpassword()
    add_data(f"{path}/users.txt", user)
    login()


def getname():
    fname = str(input("please enter your first name :\n"))
    return fname


def getlastname():
    lname = str(input("please enter your last name :\n"))
    return lname


def getmail():
    mail = str(input("please enter your email :\n"))
    return mail


def getnumber():
    number = str(input("please enter your phone number :\n"))
    return number


def getpassword():
    password = str(input("please enter a password :\n"))
    return password


def getpasswordagain():
    passwordagain = str(input("please enter your password once more:\n"))
    return passwordagain


def passwordmatch(val1, val2):
    return val1 == val2


def read_data(filepath):
    with open(filepath, 'r') as file:
        return file.read()


def is_valid_email(mail):
    lines = read_data(f"{path}/users.txt")
    linesplit = lines.split('\n')
    for line in linesplit:
        if line.find(mail) != -1:
            return False
    return re.fullmatch(EMAIL_REG, mail)


def is_valid_phone(phone):
    return re.fullmatch(PHONE_REG, phone)


def add_data(filepath, data):
    with open(filepath, 'a') as file:
        for key, value in data.items():
            if key == "phone":
                file.write('%s\n' % (value))
            else:
                file.write('%s:' % (value))
