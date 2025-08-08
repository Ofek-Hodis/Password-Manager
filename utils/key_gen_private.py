from cryptography.fernet import Fernet  # Importing Fernet to generate a key

key = Fernet.generate_key()  # The generation of the key
print(key.decode())  # Printing the key to save it and manually store it in private .env file
