from pyfiglet import Figlet
import sys
import random

# create figlet instance
figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1 or len(sys.argv) == 3:
    print('y')
    if sys.argv[1] not in ['-f','--font'] or sys.argv[2] not in fonts:
        sys.exit('Check the command line inputs')

    # set font based on given font or randomly
    if len(sys.argv) == 3:
        font = sys.argv[2]
    else:
        font = random.choice(fonts)

    figlet.setFont(font)            # set font
    str = input()                   # input user string
    print(figlet.renderText(str))   # print output


# if second_arg isEmpty():
#     font = random.choice(fonts)

