"""
BASICS

Creates the bike database, designed to create an example database for the bikes.
Not used for actual project.
"""

import geopy as gp
import random

# List of locations (assuming all of them are in Tyler, TX)
# All locations are expressed as a dictionary of the form
# {number, road/street, City, State}
LL_LL = [ '5514 S Broadway Ave, Tyler, TX 75703',
 '6106 S Broadway Ave, Tyler, TX 75703',
 '2203 W Martin Luther King Jr Blvd, Tyler, TX 75702',
 '2151 Frankston Hwy, Tyler, TX 75701',
 '420 Rose Park Dr, Tyler, TX 75702']

# Creates a database with 80 bikes and their information
with open("BKE_DB.txt", "w") as tff:
    for qq in range(0, 80):
        tff.write(random.choice(LL_LL)+': bike available'+'\n')
