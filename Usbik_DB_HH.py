"""
BASICS

User gives an address where the bike station is, and then removes one of such
from the bike database.
Then, it adds the encrypted user information to the file.
Every user needs to input a payment information mechanism, which is encrypted
using their password as a key.
Ecah line of the database contains the following information (all encrypted):
Name, Credit Card, Checked-out date
"""

import sys
import datetime
import hashlib


# Adds a new user to the list of users using the bike
# U_PERM (str): In form Address(str), Hashing(str), Credit Card(str)

def obt_bike(U_PERM):
    U_PERM1 = U_PERM.replace('\n', '')

    U_Addr = U_PERM1.split('; ')[0]
    U_NM = U_PERM1.split('; ')[1] # Username (str): Password(str)
    namu = U_NM.split(', ')[0]
    pssu = U_NM.split(', ')[1]
    # Combines both variables into a byte-string
    bCOMB = str(namu+pssu).encode('ascii')
    U_NM = str(hashlib.sha224(bCOMB).hexdigest())

    U_CRCD = U_PERM1.split('; ')[2]
    U_DREN = (datetime.datetime.now()).strftime('%Y-%m-%d %H:%M:%S')

    Cur_stats = [[], []] # [[Locations], [Bike counts]]

    # Reads the database with bikes and counts how many bikes in each place
    with open('BKE_DB.txt', 'r') as orf:
        # Reads the line and counts which time
        for leli in orf:
            dat_lit = leli.split(': ') # Splited line
            if dat_lit[0] not in Cur_stats[0]:
                Cur_stats[0].append(dat_lit[0])
                Cur_stats[1].append(0)

            # Adds one to the station name count
            for vtvt in range(0, len(Cur_stats[0])):
                if Cur_stats[0][vtvt] == dat_lit[0]:
                    Cur_stats[1][vtvt] += 1


    # Checks the user provided address and substracts one to that point
    for msms in range(0, len(Cur_stats[0])):
        if U_Addr == Cur_stats[0][msms]:
            Cur_stats[1][msms] -= 1
            break

    # Writes the updated number of available bikes and their locations
    with open('BKE_DB.txt', 'w') as nnf:
        for nn1 in range(0, len(Cur_stats[0])):
            for oo1 in range(0, Cur_stats[1][nn1]):
                nnf.write(Cur_stats[0][nn1]+': Bike available\n')

    # Appends the information to the user's information
    with open('Users_using.txt', 'a') as ttf:
        ttf.write(str(U_Addr)+', '+str(U_NM)+', '+str(U_CRCD)+', '+str(U_DREN)+'\n')

    print('User has obtained the bike, database updated')
    return None




"""
U_Addr = '420 Rose Park Dr, Tyler, TX 75702' # Example address

Cur_stats = [[], []] # [[Locations], [Bike counts]]

# Reads the database with bikes and counts how many bikes in each place
with open('BKE_DB.txt', 'r') as orf:
    # Reads the line and counts which time
    for leli in orf:
        dat_lit = leli.split(': ') # Splited line
        if dat_lit[0] not in Cur_stats[0]:
            Cur_stats[0].append(dat_lit[0])
            Cur_stats[1].append(0)

        # Adds one to the station name count
        for vtvt in range(0, len(Cur_stats[0])):
            if Cur_stats[0][vtvt] == dat_lit[0]:
                Cur_stats[1][vtvt] += 1


# Checks the user provided address and substracts one to that point
for msms in range(0, len(Cur_stats[0])):
    if U_Addr == Cur_stats[0][msms]:
        Cur_stats[1][msms] -= 1
        break

# Writes the user's information to the database, but encrypted
with open('BKE_DB.txt', 'w') as nnf:
    for nn1 in range(0, len(Cur_stats[0])):
        for oo1 in range(0, Cur_stats[1][nn1]):
            nnf.write(Cur_stats[0][nn1]+': Bike available\n')


# Name, Credit Card, Date of renting; as obtained from the phone
U_NM = 'John Smith'
U_CRCD = '2134260016668765'
U_DREN = (datetime.datetime.now()).strftime('%Y-%m-%d %H:%M:%S')

# User password, must be provided, program turns it to bytes
U_PSS = b'Password1234'

# Checks the password against the database before uploading the information
hsh_key = hashlib.sha224(U_PSS).hexdigest()

# Appends the information to the user's information
with open('Users_using.txt', 'a') as ttf:
    ttf.write(str(U_NM)+', '+str(U_CRCD)+', '+str(U_DREN)+', '+str(hsh_key)+'\n')
"""
