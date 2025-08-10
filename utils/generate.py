import random
import string


def gen_pass(length):
    # Generating a password using the random and string module in the range of length
    return ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation) for n in range(length)])

