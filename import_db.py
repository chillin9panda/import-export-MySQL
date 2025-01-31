import os
import getpass


def import_sql(option):
    host = input("MySQL host (default: localhost): ") or "localhost"
    user = input("username: ")
    password = getpass.getpass("password: ")

    if 1 == option:
        database = input("New database name: ")
        create_db_command = f'mysql -h {host} -u{user} -p{
            password} -e "CREATE DATABASE {database};"'

        os.system(create_db_command)
        print(f"New database {database} created")

    elif 2 == option:
        database = input("Existing database name: ")
    else:
        print("Invalid Option")

    sql_file = input("SQL file name to import from: ")

    import_command = f"mysql -h {host} -u {
        user} -p{password} {database} < {sql_file}"
    os.system(import_command)
    print(f"{sql_file} has been imported to {database}")


def import_menu():
    print("1. Create and import to a new database")
    print("2. Import to Exiting database")

    try:
        choice = int(input("Enter your choice(1 or 2): "))
        import_sql(choice)
    except ValueError:
        print("Invalid Option!")


import_menu()
