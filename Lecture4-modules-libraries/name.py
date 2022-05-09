import sys

'''
try:
    print("hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments")
'''

# Check for errors
if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")

# Print name tags
print("hello, my name is", sys.argv[1])