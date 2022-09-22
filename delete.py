
import os
from projmenu import projmenu


from viewall import viewall
path = os.path.dirname(os.path.abspath(__file__))


def delete(mail):
    project_id = input("enter project id:\n")
    project_found = search_project_by_id(project_id)
    print(project_found)
    if project_found:

        project_index = project_found[1]
        allprojects = viewall()
        proj = allprojects[project_index].split(":")
        # print(proj[5])
        # input("space")
        if proj[5] == mail:
            del allprojects[project_index]
            all = '\n'.join(allprojects)
            afterdelete = write_book_list_to_the_file(all)
            print(afterdelete.split('\n'))
            input("enter to menu")
            projmenu(mail)
        else:
            print("not authorized")


def write_book_list_to_the_file(allprojects):
    with open(f'{path}/projects.txt', 'w') as file:
        file.write(str(allprojects))
        return allprojects


def search_project_by_id(projectid):
    allprojects = viewall()
    for project in allprojects:
        myproject = project.split(":")
        # print(myproject[4])
        # input("enter")
        if myproject[4] == str(projectid):
            project_index = allprojects.index(project)
            print(f"project found at index {project_index} , ")
            return True, project_index
    else:
        print("book not found ")
        return False


delete("ads@gm.com")
