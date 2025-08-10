from utils.dbconfig import dbconfig  # Importing the function used to create connection with the database

from utils.password_changes import decrypt_pass  # Importing the function used to decrypt a password

# Importing rich for neater display
from rich import print as printc
from rich.console import Console
from rich.table import Table


def retrieve_entry(search):

    db = dbconfig()  # Establishing connection with the db
    cursor = db.cursor()

    query = "SELECT * FROM pm.entries"  # This will either be the final query or the base for it
    values = []

    if search:  # verifying that search is not empty
        # Creating a list of SQL conditions (one for each item in 'search')
        conditions = [f"{k} = %s" for k in search]
        query += " WHERE " + " AND ".join(conditions)  # Joining all the items in conditions with 'AND' between them
        values = list(search.values())  # Turning the values from search into a list to fill up the %s part of the query

    cursor.execute(query, values)  # Filling the query with the values
    results = cursor.fetchall()  # Retrieves all rows returned by the query

    if len(results) == 0:
        printc("[yellow][-][/yellow] No results for the search")
        cursor.close()
        db.close()
        return

    # If there is more than one result and the user wants to see them, we create a table to display the results
    if len(results) >= 1:
        # Creating the columns of the tables using the Table function of the rich module
        table = Table(title="Results")
        table.add_column("Site Name")
        table.add_column("URL")
        table.add_column("Email")
        table.add_column("Username")
        table.add_column("Password")

        # Using a loop to create a row for each result
        for i in results:  # Going over 'results' to add rows with the results of the query
            table.add_row(i[0], i[1], i[2], i[3], decrypt_pass(i[4]))

        console = Console()
        console.print(table)

    cursor.close()
    db.close()
    return
