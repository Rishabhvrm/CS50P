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