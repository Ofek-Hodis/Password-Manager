from utils.dbconfig import dbconfig  # Importing the function used to create connection with the database

from utils.password_changes import decrypt_pass  # Importing the function used to decrypt a password

# Importing rich for neater display
from rich import print as printc
from rich.console import Console
from rich.table import Table  # Imported to create the table displayed to the user after extraction


# The function used to retrieve what the user is searching based on the information inputted
def retrieve_entry(search):

    db = dbconfig()  # Establishing connection with the db
    cursor = db.cursor()

    query = "SELECT * FROM pm.entries"  # This will either be the final query or the base for it
    values = []

    if search:  # verifying that search is not empty
        conditions = [f"{k} = %s" for k in search]  # Creating a list of SQL conditions (one for each item in 'search')
        query += " WHERE " + " AND ".join(conditions)  # Joining all the items in conditions with 'AND' between them
        values = list(search.values())  # Turning the values from search into a list to fill up the %s part of the query

    cursor.execute(query, values)  # Filling the query with the values
    results = cursor.fetchall()  # Retrieves all rows returned by the query

    if len(results) == 0:  # Checking in case there are no results and displaying fitting message
        printc("[yellow][-][/yellow] No results for the search")
        cursor.close()
        db.close()
        return

    # Creation of table columns
    table = Table(title="Results")
    table.add_column("Site Name")
    table.add_column("URL")
    table.add_column("Email")
    table.add_column("Username")
    table.add_column("Password")
    # Using a loop to create a row for each result
    for i in results:  # Going over 'results' to add rows with the results of the query
        table.add_row(str(i[1]), i[2], i[3], i[4], decrypt_pass(i[5]))

    console = Console()
    console.print(table)

    cursor.close()
    db.close()
    return
