"""
BASICS

Uploads data to the server using the JSON format.
"""

from requests import put, get, delete, post

# Gets the user's provided data, requires python plugin to Android app

# The user must provide the data with the following
# US_CDE = 0 # 0: find bike; 1: get bike; 2: return bike; 3: login; 4: register new user
# US_INF = '6200 Troup Highway, Tyler, TX 75703' # User information, must be provided by java

US_CDE = 3
US_INF = 'Johnny46, NYC'

US_SGL = str(US_CDE)+': '+str(US_INF)
#'data': 'Remember the milk'

US_DATA = {US_CDE : US_SGL}

put('http://localhost:5000/todo1', data={'data':US_SGL}).json() # Do not change anything here
print('Data added')
