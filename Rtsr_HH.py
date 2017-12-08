"""
BASICS

Adds a new user to the registry of users, together with password, in the form of
username, password.
"""

import hashlib
import time


# Function that adds new user to the registry, hashed
# New_U (str): In the form Username(str), Password(str)
# Does not return anything, uploads user's hashed credentials to registry database

def add_user(New_U):
    # Username and password, provided by the app
    US_NM = str(New_U.split(', ')[0])
    US_PW = str(New_U.split(', ')[1])
    # Combines both variables into a byte-string
    bCOMB = str(US_NM+US_PW).encode('ascii')
    hsh_uk = hashlib.sha224(bCOMB).hexdigest()

    # Adds these hashes to the database
    with open('The_Reg.txt', 'a') as uuf:
        uuf.write(str(hsh_uk)+'\n')

    print('User credentials added to registry database')
    return None


"""
# Username and password, provided by the app
US_NM = 'Paul546' # Username
US_PW = 'PW435' # Password

# Combines both variables into a byte-string
bCOMB = str(US_NM+US_PW).encode('ascii')
hsh_uk = hashlib.sha224(bCOMB).hexdigest()

# Adds these hashes to the database
with open('The_Reg.txt', 'a') as uuf:
    uuf.write(str(hsh_uk)+'\n')
"""
