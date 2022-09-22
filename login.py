
import os
from projmenu import projmenu

from register import getmail, getpassword
path = os.path.dirname(os.path.abspath(__file__))
loginuser = {"email": "",
             "password": ""}


def login():
    print("--------login----------")
    if os.path.exists(f"{path}/users.txt"):
        mail = getmail()
        password = getpassword()
        authenticated = False
        authenticated = authenticate(mail, password)
        while not authenticated:
            print("user doesnt exist")
            mail = getmail()
            password = getpassword()
            authenticated = authenticate(mail, password)
        projmenu(mail)
    else:
        print('database cant be found')


def read_data(filepath):
    with open(filepath, 'r') as file:
        return file.read()


def authenticate(mail, password):
    lines = read_data(f"{path}/users.txt")
    linesplit = lines.split('\n')
    for line in linesplit:
        if line.find(mail) != -1:

            if password == line.split(":")[3]:
                return True
    return False


#login()
