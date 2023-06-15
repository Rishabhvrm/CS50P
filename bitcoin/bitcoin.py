import requests
import sys

# takes 1 command line argument as a float, sys.exit() if argument not float, missing or not a number
# Call api and check the price, handle exceptions
# outputs cost of n bitcoins in USD using thousand ,(comma separator) upto 4 digit decimal

# check length of
if len(sys.argv) < 2:
    sys.exit('Missing command-line argument')

try:
    n = float(sys.argv[1])
except:
    sys.exit('Command-line argument is not a number')


print(n)

try:
    # make a request
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
except requests.RequestException:
    sys.exit('Error Occurred')

print(r.json())