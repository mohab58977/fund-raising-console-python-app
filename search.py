from projmenu import projmenu
from viewall import viewall


def search(mail):
    date = input(
        "please enter start date of project formated as yyyy-mm-dd:\n")
    found = []
    allprojects = viewall()
    for project in allprojects:
        # print(book)
        #myproject = project.strip("\n")
        myproject = project.split(":")
        if myproject[2] == str(date):
            project_index = allprojects.index(project)
            print(f"project found at index {project_index} , ")
            found.insert(0, project)
    print(found)
    input("enter to menu")
    projmenu(mail)


#search("a")
