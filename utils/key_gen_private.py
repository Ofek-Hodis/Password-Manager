from cryptography.fernet import Fernet  # Importing Fernet to generate a key


# This page was only used once, to generate the key that is stored safely in a local .env file
key = Fernet.generate_key()  # The generation of the key
print(key.decode())  # Printing the key to save it and manually store it in private .env file
