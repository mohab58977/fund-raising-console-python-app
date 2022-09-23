from create import path, project, checkdate, checktarget, getdetails, getenddate, getstartdate, generate_new_id, gettitle, gettarget

from viewall import viewall


def edit(mail):
    data = input("enter project id:\n")

    filedata = viewall()
    for line in filedata:
        lin = line.split(":")
        if data == lin[5] and lin[6] == str(mail):
            print("----------enter new data-----------")
            newline = update(mail)
            fileda = '\n'.join(filedata)
            allprojects = fileda.replace(line, newline)
            # Write the file out again
            with open(f'{path}/projects.txt', 'w') as file:
                file.write(allprojects)
                print(allprojects.split('\n'))
                input("enter to menu")
                return True

    print("id not found or you are not authorized")
    input("enter to menu")


def update(mail):

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
    return data


# edit("ads@gm.com")
