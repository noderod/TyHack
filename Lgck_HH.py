"""
BASICS

Checks a given username and password against the database of hashes. If they have
already been covered, returns true. False if not.
"""

import hashlib

# Function that checks if an user is already on the database
# UCRED (str): User's credentials, must be in form: username(str), password(str)
def check_credentials(UCRED):
    # Username and password, provided by the app
    US_NM = str(UCRED.split(', ')[0])
    US_PW = str(UCRED.split(', ')[1])

    # Combines both variables into a byte-string
    bCOMB = str(US_NM+US_PW).encode('ascii')
    hsh_uk = str(hashlib.sha224(bCOMB).hexdigest())

    # Adds these hashes to the database
    with open('The_Reg.txt', 'r') as uuf:
        for leli in uuf:
            if hsh_uk in str(leli):
                return True
        else:
            return False





"""
# Username and password, provided by the app
US_NM = 'Paul546' # Username
US_PW = 'PW435' # Password

# Combines both variables into a byte-string
bCOMB = str(US_NM+US_PW).encode('ascii')
hsh_uk = str(hashlib.sha224(bCOMB).hexdigest())

# Adds these hashes to the database
with open('The_Reg.txt', 'r') as uuf:
    for leli in uuf:
        if hsh_uk in str(leli):
            print(True)
            break
    else:
        print(False)
"""
