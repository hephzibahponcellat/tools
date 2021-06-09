"""
Random password generator

- Generates a password of length 12
- Includes capital letters, small letters, numbers and symbols
"""

__author__ = "Hephzibah Pon Cellat Arulprakash"
__credits__ = ["Hephzibah Pon Cellat Arulprakash"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Hephzibah Pon Cellat Arulprakash"
__email__ = "poncellat@gmail.com"
__status__ = "Production"


import secrets
import string


def generate_password():
    chars = string.ascii_letters + string.digits + string.punctuation
    passwd_len = 12

    while True:
        psswd = ''.join(secrets.choice(chars) for i in range(passwd_len))

        if (
            any(c.islower() for c in psswd) &
            any(c.isupper() for c in psswd) &
            any(c.isdigit() for c in psswd) &
            any(c in string.punctuation for c in psswd)
        ):
            return psswd


if __name__ == "__main__":
    psswd = generate_password()
    print(psswd)
