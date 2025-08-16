import argparse  # Imported to facilitate the interaction with the user

# Importing rich for neater display
from rich import print as printc

from utils.password_changes import input_validate_masterpass  # Importing the function to validate master password
from utils.generate import gen_pass  # Importing the function to generate the password
import utils.add  # Importing the function to add an entry
import utils.retrieve  # Importing the function to retrieve entries

import pyperclip  # Importing pyperclip to allow copying and pasting text to the clipboard

# Not allowing automatic abbreviation to prevent length and login having the same abbreviation
parser = argparse.ArgumentParser(description='Description', allow_abbrev=False)

# Definition of the arguments to allow interaction between the user and the program
parser.add_argument('option', help='(a)dd / (e)xtract / (g)enerate')
parser.add_argument("-s", "--site", help="Site name")
parser.add_argument("-u", "--url", help="Site URL")
parser.add_argument("-e", "--email", help="Email")
parser.add_argument("-l", "--login", help="Username")
# Argument defined for generating password purposes.
parser.add_argument("--length", help="Length of the password to generate", type=int)
parser.add_argument("-c", "--copy", action='store_true', help="Copy password to keyboard")

args = parser.parse_args()

def main():
    if args.option in ["add", "a"]:  # If the user wants to add an entry
        printc("Adding")
        if args.site is None or args.url is None or args.login is None:  # Checking all crucial information was given
            if args.site is None:
                printc("[red][!][/red] Site name (-s) required")
            if args.url is None:
                printc("[red][!][/red] Site url (-u) required")
            if args.login is None:
                printc("[red][!][/red] Site login (-l) required")
            return

        if args.email is None:  # Not forcing an email value
            args.email = ""  # Changing the email to be empty instead of 'None'
        if utils.password_changes.input_validate_masterpass():  # Checking the master password with imported function
            utils.add.add_entry(args.site, args.url, args.email, args.login)  # Adding an entry to the database
            printc("[green][+][/green] Password added")
        else:
            printc("[red][!][/red] Incorrect password")

    if args.option in ["extract", "e"]:  # if the user wants to retrieve data
        printc("Extracting")
        if not utils.password_changes.input_validate_masterpass():  # Checking the master pass
            printc("[red][!][/red] Incorrect password")
            return

        search = {}  # Creating an empty dictionary to hold the search information before calling the function
        if args.site is not None:
            search["sitename"] = args.site
        if args.url is not None:
            search["siteurl"] = args.url
        if args.email is not None:
            search["email"] = args.email
        if args.login is not None:
            search["username"] = args.login

        utils.retrieve.retrieve_entry(search)  # Retrieving an entry

    if args.option in ["generate", "g"]:
        printc("Generating")
        if args.length < 1:
            printc("[red][+][/red] Specify length of the password to generate (--length). Must be greater than 0.")
            return
        password = utils.generate.gen_pass(args.length)
        pyperclip.copy(password)  # copying the password to the system clipboard
        printc("[green][+][/green] Password generated and copied to clipboard")

if __name__ == "__main__":  # Making sure the function is called only if this module is called directly, and not when imported
    main()