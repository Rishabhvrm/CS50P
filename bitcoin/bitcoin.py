import requests
import sys
import json

# takes 1 command line argument as a float, sys.exit() if argument not float, missing or not a number
# Call api and check the price, handle exceptions
# outputs cost of n bitcoins in USD using thousand ,(comma separator) upto 4 digit decimal

# check length of cmd line arguments
if len(sys.argv) != 2:
    sys.exit('Missing command-line argument')

# check if cmd argument is float
try:
    n = float(sys.argv[1])
except:
    sys.exit('Command-line argument is not a number')

# make a get request
try:
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
except requests.RequestException:
    sys.exit('Error Occurred')

# print(json.dumps(r.json(), indent = 2))

# json response similar to a python dictionary
amount_string = r.json()["bpi"]["USD"]["rate"]          # get the particular key from the json response object. bpi -> USD -> rate
amount = amount_string.replace(",", "")                 # remove the comma (,) from string response
amount_float = float(amount) * n                        # convert string to float and multiply the input to calculate the total cost
print(f'${amount_float:,.4f}')