from create import create
from viewall import viewall
from edit import edit
from delete import delete
from search import search


def projmenu(mail):

    while 1:
        print("---fund raising App -----")
        choice = input(
            "1)create project \n2)view all \n3)edit existing\n 4)delete project\n 5)search by date\n 6)logout\n 7)exit \n")
        if choice == "1":
            create(mail)
        elif choice == "2":
            viewall()
        elif choice == "3":
            edit(mail)
        elif choice == "4":
            delete(mail)
        elif choice == "5":
            search()
        elif choice == "6":
            return 0
        elif choice == "7":
            quit()

        else:
            print("---- no correct choice ----")
