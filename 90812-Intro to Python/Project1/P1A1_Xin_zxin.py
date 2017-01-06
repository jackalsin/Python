#!/usr/bin/python3
'''
@author Zhiwei Xin
@andrewID zxin
original creation date: September 4, 2016
last modification date: September 4, 2016 
This project is a measurement conversion program to help user to convert 
different units 
'''
# welcome string
WELCOME_STRING = """
---------------------- Welcome to Zhiwei Xin's Conversion ----------------------
"""
# The brief description
PROGRAM_DESCRIPTION = """\
This is a simple program that an end user to enter a floating point value 
specifying gallons of gasoline to do different sort of conversion s/he wishes to
perform\nGiven a floating point value specifying gallons of gasoline, it gives:
"""
# Options the program can do
OPTIONS = """
1. Number of liters;
2. Number of barrels of oil required to produce the gallons of gasoline 
    specified;
3. Number of pounds of CO2 produced;
4. Equivalent energy amount of ethanol gallons;
5. Price of the gasoline in US dollars.
"""
def main():
    username = ""
    while(username == ""):
        username = input("Please input your username\n").strip()
    print(WELCOME_STRING)
    print(PROGRAM_DESCRIPTION + OPTIONS)
    print("The username is " + username)


# run main function
main()