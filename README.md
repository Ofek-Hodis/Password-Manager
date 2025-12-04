# Password-Manager
A secure and user-friendly command-line password manager written in Python.  
It lets you store, retrieve, search, and generate credentials while keeping them encrypted and safe.

---

## Personal Summary
This password manager allowed me to gain practical experience with Python programming and MySQL database integration.<br>
I implemented secure password storage using different encryption and hashing techniques, and learned to handle sensitive data safely.<br>
The project also taught me how to use various Python modules effectively, manage errors, and build a functional application from start<br>
to finish, reinforcing both my programming skills and understanding of cybersecurity concepts.<br>

---

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
- MySQL 8.0.44.0 server ran locally
- The following modules installed (by using pip install module_name):
    rich<br>
    bcrypt<br>
    fernet<br>
    mysql-connector<br>
    pyperclip<br>
    python-dotenv<br>

---

## Installation
- run `git clone https://github.com/Ofek-Hodis/Password-Manager` in your chosen file location
- create a '.env' file named "secret_data.env" containing:
    DB_HOST=your_host<br>
    DB_USER=your_user<br>
    DB_PASSWORD=your_db_password<br>
    FERNET_KEY=your_generated_key (run in command line `utils/key_gen_private.py`, meant to be used once for key generation)<br>
- install relevant modules (according to the "programs used section")
- install MySQL server:
    Create root user and root password (must be stored)<br>
    Run in the command line `"C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql.exe"` -u root -p (or the relevant file location)<br>
    Run the following lines in the command line to create a new user:<br>
        `CREATE DATABASE IF NOT EXISTS password_manager CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;`<br>
        `CREATE USER IF NOT EXISTS 'appuser'@'localhost' IDENTIFIED BY 'StrongPassword123!';` (choose your name and password for the user)<br> 
        `GRANT ALL PRIVILEGES ON  *.* TO 'appuser'@'localhost';`<br>
        `FLUSH PRIVILEGES;`<br>
        `USE password_manager;`<br>

---

## Set up (after installation)
- Run `python configuration.py` in the command line (in the password-manager install location)
- Choose a master password (Write it down! It will be used to access your information)

---

## Usage instructions:
python main.py command (or -shortened command) --option additional information
Examples:
  - Generate a 16-character password:
    python main.py generate --length 16
  - Add information to the db:<db>
    python main.py add -s GitHub -u https://github.com/ -l Ofek-Hodis -e ofkhod@gmail.com
    * For the add function, entering the site (represented by -s or --site), the url (-u or --url) and the username (-l or --login) is required. The email (-e or --email) is optional.
    * After choosing information the password input will be safely prompted, and then hashed before stored.

---

## Security notes
The master password cannot be encrypted, as it was crpyted using bcrypt. It must be remembered or stored somewhere secure.<br>
User passwords can be decrypted only using the key generated using utils/generate.py and stored in the '.env' file localy. Passwords only be encrypted using this key to allow decryption.



    
