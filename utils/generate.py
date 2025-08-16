import random  # Importing random to randomly choose the characters
import string  # Importing the string module to define what characters to use when randomizing

def gen_pass(length):
    # Generating a password using the random and string module in the range of length
    return ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation) for n in range(length)])

