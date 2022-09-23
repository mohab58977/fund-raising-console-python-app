from create import path


def viewall():
    list = []
    try:
        fileobj = open(f"{path}/projects.txt")
    except Exception as e:
        print("---- error happened while openeing the file .. try again ")
        return False
    else:
        projects = fileobj.readlines()
        fileobj.close()
        for project in projects:
            mypro = project.strip("\n")
            list.append(mypro)
        print(list)
        input("enter to continue")
        return list
