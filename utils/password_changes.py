from cryptography.fernet import Fernet
from dotenv import load_dotenv  # Importing the function allowing to import data from a .env file
import os  # Allows Python to interact with the os, needed for the communication with the .env file

import getpass  # Importing a function allowing hidden input for the password
import bcrypt  # Importing bcrypt for master password verification

from utils.dbconfig import dbconfig  # Importing the function used to create connection with the database
# Importing rich for neater display
from rich import print as printc


load_dotenv()  # Loading the .env file
key = os.getenv("fernet_key")  # Pulling the encryption key generated using Fernet and stored in the .env file
f = Fernet(key)  # Creating a Fernet encryption object to execute actions like encrypt() or decrypt()



# Defining a function to hash the master password
def hash_masterpass(password):
    password_bytes = password.encode('utf-8')  # Converting the password to bytes in order to encrypt it
    hashed = bcrypt.hashpw(password_bytes, bcrypt.gensalt())  # hashing the password with a bcrypt generated salt
    return hashed.decode('utf-8')  # Returning the hashed password as a string so that  it can be stored in the db


# Creating a function to crypt a given password, will be used for the masterpass
def encrypt_pass(p):
    # We turn the string into bytes using .encode() and then encrypt it
    encrypted = f.encrypt(p.encode())
    return encrypted.decode()  # Turning it back to a string to return it as such


# Creating a function to decrypt a given password
def decrypt_pass(p):
    p_bytes = p.encode()  # Turning the encrypted password string to bytes
    decrypted_bytes = f.decrypt(p_bytes)  # Decrypting the given password using Fernet
    decrypted_p = decrypted_bytes.decode()  # Turning it back to a string
    return decrypted_p


def input_validate_masterpass():
    # Getting the input to validate the master password and converting it to bytes
    master_password_bytes = getpass.getpass("Master password: ").encode()

    db = dbconfig()  # Connecting to db
    cursor = db.cursor()
    query = "SELECT masterpass_hash FROM pm.secrets LIMIT 1"  # Getting the master password from the 'secrets' table
    try:
        cursor.execute(query)  # Executing query
        results = cursor.fetchone()  # Saving the master password to a variable
        password = results[0]
    except Exception as e:
        printc("An error occurred when trying to get the password from the db")
        return False
    if bcrypt.checkpw(master_password_bytes, password.encode()):  # Verifying the password
        printc("Password correct")
        return True
    printc("Password incorrect")  # In case the password is incorrect the function notifies the user and returns 'False'
    return False

