# registration
"""

    console application for library


    add , edit , delete , display information of the books

    create:
        title , no_of_pages, author_name

"""
from register import register
#from login import login



def mainmenu():
    while 1 :
        print("---fund raising App -----")
        choice= input("1)login \n2)register \n3)exit \n")
        if choice =="1":
          #  login()
          print(1)
        elif choice =="2":
          #  register()
          print(1)
        elif choice =="3":
            return 0
        else:
            print("---- no correct choice ----")
            return mainmenu()

mainmenu()

# login_menu = ["Register", "Sign in", "Exit"]

# auth_menu = ["List All Projects", "Create Project",
#              "Edit Project", "Delete Project", "Logout"]

