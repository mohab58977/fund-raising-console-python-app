
import os

from projmenu import projmenu
path = os.path.dirname(os.path.abspath(__file__))
loginuser = {"email": "",
             "password": ""}


def login():
    print("--------login----------")
    if os.path.exists(f"{path}/users.txt"):
        mail = getmail()
        password = getpassword()

        authenticated = authenticate(mail, password)
        while not authenticated:
            print("user doesnt exist")
            mail = getmail()
            password = getpassword()
            authenticated = authenticate(mail, password)
        projmenu(mail)
    else:
        print('database cant be found')
        return False


def getpassword():
    password = str(input("please enter a password :\n"))
    return password


def read_data(filepath):
    with open(filepath, 'r') as file:
        return file.read()


def getmail():
    mail = str(input("please enter your email :\n"))
    return mail


def authenticate(mail, password):
    lines = read_data(f"{path}/users.txt")
    linesplit = lines.split('\n')
    for line in linesplit:
        lin = line.split(':')
        if line.find(mail) != -1:

            if password == line.split(":")[3]:
                return True
    return False


# login()
