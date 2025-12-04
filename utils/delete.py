from getpass import getpass  # Function used to get input without displaying the password
from utils.dbconfig import dbconfig  # Importing the function used to create connection with the database
from utils.password_changes import encrypt_pass  # Importing the function used to encrypt a password

# Importing rich print for neater display
from rich import print as printc

#Function to delete an entry from the db
def delete_entry(sitename, username):
    password = getpass("Password: ")  # Get the password

    db = dbconfig()
    cursor = db.cursor()
    query = "DELETE FROM pm.entries WHERE sitename = %s AND username = %s"
    cursor.execute(query, (sitename, username))
    db.commit()

    if cursor.rowcount == 1:
        printc(f"[green][-][/green]Deleted the entry for {sitename} / {username}.")
    else:
        print("[red][-][/red]No matching entry found.")

    cursor.close()
    db.close()


