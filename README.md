# Password-Manager
A secure and user-friendly command-line password manager written in Python.  
It lets you store, retrieve, search, and generate credentials while keeping them encrypted and safe.

---

## Personal Summary
This password manager allowed me to gain practical experience with Python programming and MySQL database integration.
I implemented secure password storage using different encryption and hashing techniques, and learned to handle sensitive data safely.
The project also taught me how to use various Python modules effectively, manage errors, and build a functional application from start
to finish, reinforcing both my programming skills and understanding of cybersecurity concepts.

## Features
- **Store credentials**: Site name, URL, email, username, password.
- **Search**: Find credentials by name, URL, email, or username.
- **Password generation**: Create strong random passwords of custom length.
- **Encryption**: Stored passwords are encrypted using **Fernet**.
- **Master password security**: Protected with **bcrypt** hashing.
- **Neat output**: Neatly formatted tables using 'rich'.
- **Clipboard support**: Copy passwords securely with 'pyperclip'.
- **Simple interaction**: User interaction is simplified using argeparse

---

## Programs used
- Python 3.9
- MySQL server ran locally
- '.env' file containing:
    DB_HOST=your_host
    DB_USER=your_user
    DB_PASSWORD=your_db_password
    FERNET_KEY=your_generated_key (using utils/generate.py, meant to be used once for key generation)
- The following modules installed (by using pip install module_name):
    rich
    bcrypt
    fernet
    mysql-connector
    pyperclip
    python-dotenv

---

## Installation
- install the relevant programs and modules
- Create said '.env' file
- git clone https://github.com/Ofek-Hodis/Password-Manager

---

## Usage instructions:
python main.py command (or -shortened command) --option additional information
Examples:
  - Generate a 16-character password:
    python main.py generate --length 16
  - Add information to the db:
    python main.py add -s GitHub -u https://github.com/ -l Ofek-Hodis -e ofkhod@gmail.com
    * For the add function, entering the site (represented by -s or --site), the url (-u or --url) and the username (-l or --login) is required. The email (-e or --email) is optional.
    * After choosing information the password input will be safely prompted, and then hashed before stored.

---

## Security notes
The master password cannot be encrypted, as it was crpyted using bcrypt. It must be remembered or stored somewhere secure.
User passwords can be decrypted only using the key generated using utils/generate.py and stored in the '.env' file localy. Passwords only be encrypted using this key to allow decryption.



    
