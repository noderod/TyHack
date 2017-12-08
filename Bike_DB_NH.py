"""
BASICS

Checks the bike database for a specific bike, if none are found, returns a message.
If several are found, it returns the location of the closest station that has it.
Designed to be communicated with Bike_Usage_NH.py, user API.
Asks the user if he is interested in it, if he is, removes the bike example from
the bike database and adds the client information to the users database.
"""

import geopy
from geopy.distance import vincenty
import time


# Function which returns the closest bike
# UAD (str): User's address

def biksta(UAD):
    # Finds all the current stations with bikes in them
    Ava_stat = []

    with open('BKE_DB.txt', 'r') as ff:
        for ll in ff:
            New_stat = ll.split(': ')[0]
            if New_stat not in Ava_stat:
                Ava_stat.append(New_stat)


    # Finds the information of the user address
    geolocator = geopy.geocoders.Nominatim()
    u_loc = geolocator.geocode(UAD)
    # Computes the coordinates
    u_cord = (u_loc.latitude, u_loc.longitude)
    time.sleep(0.75) # Sleeps

    # Finds the closest station from the user location
    Ava_dist = []

    # End result (arr): [Loc 1, Loc 2, ...] -> Loc 1 = [Name, distance]
    for stbk in Ava_stat:
        # Obtains the coordinates
        sta_loc = geolocator.geocode(stbk)
        sta_cords = (sta_loc.latitude, sta_loc.longitude)
        Ava_dist.append([stbk, vincenty(sta_cords, u_cord).miles])
        time.sleep(1)


    # Returns the closest bike station
    clo_stat = sorted(Ava_dist, key = lambda x: x[1])[0]

    return 'Closest station:\n'+str(clo_stat[0])+'; '+str(clo_stat[1])+' m'


"""
# Finds all the current stations with bikes in them
Ava_stat = []

with open('BKE_DB.txt', 'r') as ff:
    for ll in ff:
        New_stat = ll.split(': ')[0]
        if New_stat not in Ava_stat:
            Ava_stat.append(New_stat)

print(Ava_stat)

# Gets the user current address in a text box
U_Addr = '6200 Troup Highway, Tyler, TX 75703'

# Finds the information of the user address
geolocator = geopy.geocoders.Nominatim()
u_loc = geolocator.geocode(U_Addr)
# Computes the coordinates
u_cord = (u_loc.latitude, u_loc.longitude)
time.sleep(1) # Sleeps

# Finds the closest station from the user location
Ava_dist = []

# End result (arr): [Loc 1, Loc 2, ...] -> Loc 1 = [Name, distance]
for stbk in Ava_stat:
    print(stbk)
    # Obtains the coordinates
    sta_loc = geolocator.geocode(stbk)
    sta_cords = (sta_loc.latitude, sta_loc.longitude)
    Ava_dist.append([stbk, vincenty(sta_cords, u_cord).miles])
    time.sleep(1)


# Prints the closest one
print(Ava_dist)
print(sorted(Ava_dist, key = lambda x: x[1])[0])
"""
