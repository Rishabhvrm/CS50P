from pyfiglet import Figlet
import pyfiglet
import sys
import random

# create figlet instance
figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1 or len(sys.argv) == 3:

    # check input conditions
    # if the first argument is not -f or --font
    # or the second argument is not a valid font
    # then exit 
    if sys.argv[1] not in ['-f','--font'] or sys.argv[2] not in fonts:
        sys.exit('Invalid usage')

    # set font based on given font or randomly
    font = sys.argv[2] if len(sys.argv) == 3 else random.choice(fonts)
    str = input()                                                           # input user string
    print(pyfiglet.figlet_format(str, font = font))                         # print output

else:
    sys.exit('Invalid usage')