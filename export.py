import os


def export_from_sql():
    host = input("MySQL host (default: localhost): ") or "localhost"
    user = input("username: ")
    password = input("password: ")
    database = input("Database name: ")
    output_file = input("Output file name: ")

    command = f"mysqldump -h {host} -u {user} -p{
        password} {database} > {output_file}"

    os.system(command)

    print(f"Database {database} has been exported to {output_file}.")


export_from_sql()
