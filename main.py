from register import register
from login import login

def mainmenu():
    while 1:
        print("---fund raising App -----")
        choice = input("1)login \n2)register \n3)exit \n")
        if choice == "1":
            
            login()
        elif choice == "2":
            register()
        elif choice == "3":
            quit()

        else:
            print("---- no correct choice ----")
            mainmenu()


mainmenu()

# login_menu = ["Register", "Sign in", "Exit"]

# auth_menu = ["List All Projects", "Create Project",
#              "Edit Project", "Delete Project", "Logout"]
