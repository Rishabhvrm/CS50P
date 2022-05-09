import random
# from random import choice

# using choice(seq)
coin = random.choice(["heads", "tails"])
print(coin)

# using randint(a,b)
randomInteger = random.randint(1,10)
print(randomInteger)

# using shuffle(x)
# it shuffles the argument in place
cards = ["jack", "queen", "king"]
random.shuffle(cards)
print(cards)
