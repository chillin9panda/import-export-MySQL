import os
import getpass


def export_from_sql(option):
    host = input("MySQL host (default: localhost): ") or "localhost"
    user = input("username: ")
    password = getpass.getpass("password: ")
    database = input("Database name: ")

    if 1 == option:
        output_file = input("Output file name for table structure: ")
        command = f"mysqldump -h {host} -u {user} -p{
            password} --no-data {database} > {output_file}"
        os.system(command)
        print(f"Table structure of database {
              database} has been exported to {output_file}.")

    elif 2 == option:
        output_file = input("Output file name for data: ")
        command = f"mysqldump -h {host} -u {user} -p{
            password} --no-create-info {database} > {output_file}"
        os.system(command)
        print(f"Data from database {
              database} has been exported to {output_file}.")
    elif 3 == option:
        output_file = input("Output file name for table for full database: ")
        command = f"mysqldump -h {host} -u {user} -p{
            password} {database} > {output_file}"
        os.system(command)
        print(f"Full database {database} has been exported to {output_file}.")
    else:
        print("Invalid Option.")


def menu():
    print("Choose an Export option:")
    print("1. Export table creation statments only")
    print("2. Export data insertion statments only")
    print("3. Export All")

    try:
        choice = int(input("Enter your choice(1/2/3): "))
        export_from_sql(choice)
    except ValueError:
        print("Invalid Option!")


menu()
