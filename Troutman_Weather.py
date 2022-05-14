# Calvin Troutman
# CIS245 Introduction to Programming
# Weather Project
#
# This program will allow a user to get the weather for a location using their city or zip code.
#
# Requirements:
# Create a Python Application which asks the user for their zip code or city.
# Use the zip code or city name in order to obtain weather forecast data from: http://openweathermap.org/
# Display the weather forecast in a readable format to the user.
# Use comments within the application where appropriate in order to document what the program is doing.
# Use functions including a main function.
# Allow the user to run the program multiple times.
# Validate whether the user entered valid data.  If valid data isn’t presented notify the user.
# Use the Requests library in order to request data from the webservice.
# Use Python 3.
# Use try blocks when establishing connections to the webservice. You must print a message to the user \
#   indicating whether or not the connection was successful.


import requests
import time
import json


print("")


KEY = "86d34b2798f06ccbb22e88370bf473d5"
URL = "http://api.openweathermap.org/geo/1.0/zip?zip=" + "" + "&appid="+ "KEY"


def main():
    headers = {'Accept': 'application/vnd.github.v3+json'}
    local = input("Enter ZIP code: ")

    r = requests.get(URL, headers=headers)

    myjson = r.json()
    print(myjson.get("lat"))
