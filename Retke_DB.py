"""
BASICS

A program that searches the user's database and, when provided with the password,
takes that user's information off the database and adds one more bike to the
appropriate location
"""


import hashlib


# Retruns the bike to the station and erases the user from the using pool
# UINF (str): In form: Station address(str); Name, Password
# Erases the name from the database

def retbik(UNIF):
    UNIF1 = UNIF.split('; ')
    ST_AD = UNIF1[0] # Station name

    # Username and password, provided by the app
    US_NM = str(UNIF1[1].split(', ')[0])
    US_PW = str(UNIF1[1].split(', ')[1])
    # Combines both variables into a byte-string
    bCOMB = str(US_NM+US_PW).encode('ascii')
    hsh_uk = str(hashlib.sha224(bCOMB).hexdigest())

    # Opens the user's database and creates a new one
    with open('Users_using.txt', 'r') as rrf:
        with open('Users_using1.txt', 'w') as wwf:
            for line in rrf:
                if hsh_uk in line:
                    continue
                else:
                    wwf.write(line+'\n')

    with open('Users_using.txt', 'w') as wwf:
        with open('Users_using1.txt', 'r') as rrf:
            for line in rrf:
                wwf.write(line+'\n')

    with open('BKE_DB.txt', 'a') as bbf:
        bbf.write(ST_AD+': Bike available\n')

    print('Bike returned to station, user\'s information deleted')
    return None


"""
# Opens the user's database and creates a new one
with open('Users_using.txt', 'r') as rrf:
    with open('Users_using1.txt', 'w') as wwf:
        for line in rrf:
            if hsh_key in line:
                continue
            else:
                wwf.write(line+'\n')

with open('Users_using.txt', 'w') as wwf:
    with open('Users_using1.txt', 'r') as rrf:
        for line in rrf:
            wwf.write(line+'\n')

with open('BKE_DB.txt', 'a') as bbf:
    bbf.write(ST_AD+': Bike available\n')
"""
