import sys

'''
try:
    print("hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments")
'''

# Check for errors
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
#elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

# taking a 'slice' of the list
for arg in sys.argv[1:]:
    print(arg)

# Print name tags
#print("hello, my name is", sys.argv[1])