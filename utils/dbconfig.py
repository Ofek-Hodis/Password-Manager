import mysql.connector

from dotenv import load_dotenv  # Importing the function allowing to import data from a .env file
import os  # Allows Python to interact with the os, needed for the communication with the .env file

# Importing rich for neater display
from rich import print as printc
from rich.console import Console

# Importing a command used to navigate to a specific file type (will be used to locate the .env file)
from pathlib import Path

console = Console()

# Loading the variables from the .env file by saving the path and giving it to the function load_dotenv()
env_path = Path(__file__).resolve().parent / "secret_data.env"
load_dotenv(dotenv_path=env_path)

print("Host:", os.getenv("DB_HOST"))
print("User:", os.getenv("DB_USER"))
print("Password:", os.getenv("DB_PASSWORD"))


# Function to create a database
def dbconfig():
    db = None  # Defining db so if the try fails the function will not crash
    try:
        db = mysql.connector.connect(
            host=os.getenv("DB_HOST"),  # taking the host, user and password from the .env file
            user=os.getenv("DB_USER"),
            passwd=os.getenv("DB_PASSWORD")
        )
    # In case the creation didn't work, post an
    except Exception as e:
        console.print_exception(
            show_locals=True)  # Print detailed error traceback including local variables for easier debugging

    return db
