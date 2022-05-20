# Calvin Troutman
# CIS245 Introduction to Programming
# File Writer
#
# This week we will create a program that performs file processing activities. Your program this week will
# use the OS library in order to validate that a directory exists before creating a file in that directory.
# Your program will prompt the user for the directory they would like to save the file in as well as the name
# of the file. The program should then prompt the user for their name, address, and phone number. Your program
# will write this data to a comma separated line in a file and store the file in the directory specified by the user.


import os
import os.path


def createFile():
    directorName = input(f"Directory Name:  ")
    fileName = input(f"File Name:  ")

    if os.path.exists(fileName):   # checks to see if the directory exists.
        print("This file already exists.")
    else:
        print("This is a new file.")

    if os.path.isdir(directorName):   # check to see if the file already exists.
        print("This directory exists.")

    name = input(f"Enter your name:  ")  # asks user for name, address, phone numer to add to list
    address = input(f"Enter your address:  ")
    phoneNumber = input(f"Enter your phone number:  ")

    filePath = directorName + fileName
    with open(filePath, 'w') as fileHandle:
        fileHandle.write(",".join([name, address, phoneNumber]))  # writes the user info to file
    with open(filePath, 'r') as fileHandle:
        data = fileHandle.read().split(',')  # put user info into a list, got from https://eldoyle.github.io/PythonIntro/08-ReadingandWritingTextFiles/
        print(data)   # prints out the data


createFile()
