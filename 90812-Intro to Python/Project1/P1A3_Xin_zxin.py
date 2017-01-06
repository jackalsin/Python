#!/usr/bin/python3
'''
@author Zhiwei Xin
@andrewID zxin
original creation date: September 4, 2016
last modification date: September 4, 2016 
This project is a measurement conversion program to help user to convert 
different units 
'''

import re

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
# regular expression to determine if a string is a float number.
# Dont use RE to determine Positive, -0.0 can be tricky.
FLOAT_NUMBER_PATTERN = "^[+-]?[0-9]*\.?[0-9]+"

# the pattern compiled
IS_FLOAT_PATTERN = re.compile(FLOAT_NUMBER_PATTERN)

# constant defined
# how many pounds of co2 per gallon
POUNDS_OF_CO2_PER_GALLON = 20

# barrel of oil produces 19.5 gallons of gas 
GALLON_OF_GAS_PER_BARREL_OF_OIL = 19.5

# Liter to gallon Rational
LITER_TO_GALLON_RATIO = 3.7854

# Energy 1 gallon of gas produced in BTU
ENERGY_PER_GALLON_OF_GAS = 115000

# Energy 1 gallon of ethanol produced in BTU
ENERGY_PER_GALLON_OF_ETHANOL = 75700

# unit price of gas in US dollars
DOLLAR_PER_GALLON = 4.00

def main():
    username = ""
    while(username == ""):
        username = input("Please input your username\n").strip()
    # print out the welcome message
    print(WELCOME_STRING)
    print(PROGRAM_DESCRIPTION + OPTIONS)
    print("The username is " + username)

    # get the gallon of gas
    inputVal = input("""How many gallons of gasoline you want to convert? \
or -1 to exit\n""")
    while(inputVal != "-1" and not isValidFloatNumber(inputVal)):
        inputVal = input("Give me a valid float number or type '-1' to exit\n")
    if(inputVal != "-1"):
        gallonsOfGas = float(inputVal.strip())
        op = ""
        # get option of menu
        while(op != "-1"):
            if (op == "1"):
                # display number of liters
                print("Number of liters = %.4f" % gallonsToLiter(gallonsOfGas))
                op = ""                
            elif (op == "2"):
                # Number of barrels of oil required to produce gallons of gas
                print("Number of barrels of oil required = %.4f" % \
                        gallonsToBarrelOfOils(gallonsOfGas))
                op = ""                
            elif (op == "3"):
                # Number of pounds of CO2 produced
                print("Number of pounds of CO2 produced = %.4f" % \
                            co2Produced(gallonsOfGas))
                op = ""
            elif (op == "4"):
                # Equivalent energy amount of ethanol gallons
                print("Equivalent energy amount of ethanol in gallons = %.4f" \
                        % equivalentEnergyAmountOfEthanolGallons(gallonsOfGas))
                op = ""            
            elif (op == "5"):
                # Price of the gasoline in US dollars
                print("Price of the gasoline in US dollars = %.2f" % \
                            priceOfGasInDollars(gallonsOfGas))
                op = ""
            elif (op == "-1"):
                break;
            else:
                displayMenu()
                op = input("please enter your choice\n").strip()
            
# This displays the menu of the program.
def displayMenu():
    print('''\
------------------------------------ Menu --------------------------------------
    ''')
    print(OPTIONS)
    print("Or type '-1' to exit")
    
'''
    To determine if a number is a positive float Number
    @param number a string to determine
'''
def isValidFloatNumber(number):
    try:
        float(number)
        return True
    except ValueError:
        return False

# ----------------- five options results --------------------------------------

# Number of liters;
def gallonsToLiter(gallons):
    return gallons * LITER_TO_GALLON_RATIO

# Number of barrels of oil required to produce the gallons of gasoline specified
def gallonsToBarrelOfOils(gallons):
    return gallons / GALLON_OF_GAS_PER_BARREL_OF_OIL

# Number of pounds of CO2 produced;
def co2Produced(gallons):
    return gallons * POUNDS_OF_CO2_PER_GALLON;

# Equivalent energy amount of ethanol gallons;
def equivalentEnergyAmountOfEthanolGallons(gallonsOfGas):
    return gallonsOfGas * ENERGY_PER_GALLON_OF_GAS /ENERGY_PER_GALLON_OF_ETHANOL
# Price of the gasoline in US dollars.
def priceOfGasInDollars(gallonsOfGas):
    return DOLLAR_PER_GALLON * gallonsOfGas

# run main function
main()

######################### Test File ###############################

# def testIsFloatNumber():
#     assert(isValidFloatNumber("123") == True)
#     assert(isValidFloatNumber("123.4") == True)
#     assert(isValidFloatNumber("-123") == False)
#     assert(isValidFloatNumber("-0") == True)
#     assert(isValidFloatNumber("-0.0") == True)
#     assert(isValidFloatNumber("2") == True)
#     assert(isValidFloatNumber("0") == True)
#     assert(isValidFloatNumber("0.0") == True)

# def runTest():
#     testIsFloatNumber()
#     print("All test passed")

# runTest()