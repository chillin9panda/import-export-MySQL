from src import import_db as idb
from src import export_db as edb


def run():
    option = None
    while 0 != option:
        print("1. Import DB")
        print("2. Export DB")
        print("0. Exit")
        try:
            option = int(input("Option: "))
        except ValueError:
            print("Invalid Option!")

        if 1 == option:
            idb.import_menu()
        elif 2 == option:
            edb.export_menu()
        elif 0 == option:
            print("Exiting,,,")
        else:
            print("Invalid OPtion!")


run()
