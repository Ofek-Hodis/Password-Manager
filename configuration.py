from utils.dbconfig import dbconfig  # importing the function creating a database
import sys  # Imported for the use of sys.exit()
import getpass  # Imported to be able to get a password input without displaying it

import bcrypt  # Imported for strong password encrypting

# Importing rich for neater display
from rich import print as printc
from rich.console import Console

from utils.password_changes import hash_masterpass

console = Console()


def config():
    # Creating a database using the imported function
    db = dbconfig()
    cursor = db.cursor()

    printc("[green][+] Creating new config [/green]")
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS pm")
    except Exception as e:
        printc("[red][!] An error occurred while trying to create db.")
        console.print_exception(show_locals=True)
        sys.exit(0)
    printc("[green][+][/green] Database 'pm' created")

    # Create a table to store the MP, with an id column (if it does not exist already)
    #  VARCHAR is more efficient than TEXT NOT NULL, and the hashed password will never be too long for it
    query = ("CREATE TABLE IF NOT EXISTS pm.secrets (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, masterpass_hash "
             "VARCHAR(100))")
    res = cursor.execute(query)  # storing the results of the execution of the query
    printc("[green][+][/green] Table 'secrets' created")

    # Create a table to store passwords and relevant information, with an id column (if it does not exist already)
    # VARCHAR(254), because that is the length limit of a mail
    query = ("CREATE TABLE IF NOT EXISTS pm.entries (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, sitename "
             "VARCHAR(100) NOT NULL, "
             "siteurl TEXT NOT NULL, "
             "email VARCHAR(254), username VARCHAR(100), "
             "password TEXT NOT NULL)")
    res = cursor.execute(query)  # storing the results of the execution of the query
    printc("[green][+][/green] Table 'entries' created")

    while True:  # Infinite loop to get two identical password inputs
        mp = getpass.getpass("Choose a MASTER PASSWORD")  # Getting a password input without displaying it
        # Verifying the passwords are the same and not empty
        if mp == getpass.getpass("Please verify your password") and mp != "":
            printc("[green][+][/green] Password successfully created")
            break
        if mp == "":  # Checking the reason for the error to display a clear explanation
            printc("[yellow][-] The password can not be empty, please try again. [/yellow]")
        else:
            printc("[yellow][-] The passwords do not match, please try again. [/yellow]")

    # Using the previously created function to hash the password before inserting it
    hashed_mp = hash_masterpass(mp)

    # Inserting the hashed password to the secrets table
    query = "INSERT INTO pm.secrets (masterpass_hash) values (%s)"
    # To execute this query, hashed_mp is converted to a 1 tuple using the ',' (otherwise python gives an error)
    cursor.execute(query, (hashed_mp,))
    db.commit()

    printc("[green][+][/green] The password has been added to the database")
    printc("[green][+] Configuration done![/green]")

    cursor.close()
    db.close()


config()
