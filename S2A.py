"""
BASICS

Returns the information from the database, but does not process it.
"""

from requests import put, get


# Obtains the pure data from the server
# No inputs needed, only by default
# Returns a JSON object which can be operated as a dictionary

def purdat():
    return get('http://localhost:5000/todo1').json()


# Processes the obtained data and returns certain things
# No inputs needed
# Returns a string with the resultant information

def fininf():
    return purdat()['todo1']


# Using the user given input, returns several things depending on the user's command
def resdata():
    UU_PRV = fininf().split(': ') # User provided data
    Command = float(UU_PRV[0])

    # Depends on what the user provides, the program will compute one thing or another\
    if Command == 0:
        # Finds closest bike
        import Bike_DB_NH
        return Bike_DB_NH.biksta(UU_PRV[1])

    elif Command == 1:
        # Gets a bike
        import Lgck_HH
        # Validates the user's credentials, if they are not validated, nothing works
        # Gets the bike
        import Usbik_DB_HH
        return Usbik_DB_HH.obt_bike(UU_PRV[1])


    elif Command == 2:
        # Returns the bike to an available station
        import Retke_DB
        return Retke_DB.retbik(UU_PRV[1])

    elif Command == 3:
        # Checks the user login information
        import Lgck_HH
        Validat = Lgck_HH.check_credentials(UU_PRV[1]) # User's credentials validations
        if Validat == True:
            print('User\'s credentials validated')
            return True
        else:
            print('Incorrect username or password')
            return False

    elif Command == 4:
        # Registers new user
        import Rtsr_HH
        return Rtsr_HH.add_user(UU_PRV[1])
