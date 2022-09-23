

from datetime import datetime
import time
import re
import os
path = os.path.dirname(os.path.abspath(__file__))

# Validate date


DATE_REG = re.compile(
    r'^(\d{4})-(0[1-9]|1[0-2]|[1-9])-([1-9]|0[1-9]|[1-2]\d|3[0-1])$')


project = {"title": "", "start": "", "end": "",
           "target": "", "id": "", "owner": ""}


def create(mail):
    print("----------create project------------")
    project["id"] = generate_new_id()
    project["title"] = gettitle()
    project["details"] = getdetails()
    start = getstartdate()
    end = getenddate()
    while not checkdate(start, end):
        print("start and end dates must be in correct format")
        start = getstartdate()
        end = getenddate()
    target = gettarget()
    while not checktarget(target) == target:
        print("must be positive integer")
        target = gettarget()
    project["owner"] = mail
    project["target"] = target
    project["start"] = start
    project["end"] = end

    proj = []
    proj.insert(0, project["title"])
    proj.insert(1, project["details"])
    proj.insert(2, project["start"])
    proj.insert(3, project["end"])
    proj.insert(4, project["target"])
    proj.insert(5, project["id"])
    proj.insert(6, project["owner"])
    data = ":".join(proj)
    write_project_to_the_file(data)
    input("successful \n press enter to menu")


def generate_new_id():
    id = round(time.time())
    return str(id)


def gettitle():
    return input("please enter title:\n")


def getdetails():
    return input("please enter details:\n")


def getstartdate():
    return input("please enter the campaign start date formatted as YYYY-MM-DD:\n")


def getenddate():
    return input("please enter campaign's end date formatted as YYYY-MM-DD:\n")


def gettarget():
    return input("please enter campaign's target:\n")


def checktarget(num):
    for i in num:
        if not (i.isdigit()):
            return False

    return num


def checkdate(date1, date2):

    if re.fullmatch(DATE_REG, date1) and re.fullmatch(DATE_REG, date2):
        myDate = datetime.strptime(date1, "%Y-%m-%d")
        myDate2 = datetime.strptime(date2, "%Y-%m-%d")
        # Today's Date is 2022-06-27
        todayDate = datetime.now()

        if myDate.date() < myDate2.date() and myDate.date() > todayDate.date():
            return True
    else:
        return False


def write_project_to_the_file(project):
    project = f"{project}\n"
    try:
        with open(f"{path}/projects.txt", 'a') as file:
            file.write(project)
    except Exception as e:
        print(e)
        return False


# create("ads@gm.com")
