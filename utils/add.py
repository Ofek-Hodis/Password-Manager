from getpass import getpass  # Function used to get input without displaying the password
from utils.dbconfig import dbconfig  # Importing the function used to create connection with the database
from utils.password_changes import encrypt_pass  # Importing the function used to encrypt a password

# Importing rich print for neater display
from rich import print as printc


# Function to add entries to the table
def add_entry(sitename, siteurl, email, username):
    password = getpass("Password: ")  # Get the password

    # Add the information to the db
    db = dbconfig()
    cursor = db.cursor()
    query = "INSERT INTO pm.entries (sitename, siteurl, email, username, password) values(%s, %s, %s, %s, %s)"

    # Storing the values and encrypting the password
    val = sitename, siteurl, email, username, encrypt_pass(password)
    cursor.execute(query, val)  # Execution of query
    db.commit()  # Saving changes to database

    printc("[green][+][/green] Entry added successfully")

    cursor.close()  #Closing the cursor and the db after interacting with it
    db.close()
