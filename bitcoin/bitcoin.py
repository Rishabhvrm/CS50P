import requests
import sys

# takes 1 command line argument as a float, sys.exit() if argument not float, missing or not a number
# Call api and check the price, handle exceptions
# outputs cost of n bitcoins in USD using thousand ,(comma separator) upto 4 digit decimal

if len(sys.argv) < 2:
    sys.exit('Missing command-line argument')

if type(sys.argv[1]) != float:
    sys.exit('Command-line argument is not a number')

