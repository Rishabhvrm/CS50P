import random
# coin = random.choice(["heads", "tails"])

# use directly 'import' or use 'from' and then function name

from random import choice

# choose a random value from the given sequence
coin = choice(["heads", "tails"])
print(coin)

# choose a random number inclusive of the parameters
number = random.randint(1,10)
print(number)

# shuffle the argument 'in-place'
cards = ['jack', 'queen', 'king']
random.shuffle(cards)
print(cards)


# STATISTICS
import statistics

print(statistics.mean([100,90]))


# COMMAND-LINE ARGUMENTS
# sys.argv
import sys

# check for errors
if len(sys.argv) < 2:
    sys.exit('Too few arguments')          # by sys.exit we are making sure that program would exit and not reach further lines of code
elif len(sys.argv) > 2:
    sys.exit('Too many arguments')


# print name
print('hello, my name is', sys.argv[1])


# SLICE in strings