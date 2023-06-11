from pyfiglet import Figlet
import pyfiglet
import sys
import random

# create figlet instance
figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1 or len(sys.argv) == 3:
    print('y')
    # check input conditions
    if sys.argv[1] not in ['-f','--font'] or sys.argv[2] not in fonts:
        sys.exit('Invalid usage')

    # set font based on given font or randomly
    # if len(sys.argv) == 3:
    #     font = sys.argv[2]
    # else:
    #     font = random.choice(fonts)

    font = sys.argv[2] if len(sys.argv) == 3 else random.choice(fonts)
    print(font)

    # figlet.setFont(font)            # set font
    str = input()                   # input user string
    # print(figlet.renderText(str))   # print output

    output = pyfiglet.figlet_format(str, font = font)
    print(output)

else:
    sys.exit('Invalid usage')