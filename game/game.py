import random

n = input('Level: ')

# choose a random number inclusive of the parameters
number = random.randint(1,n)
print(number)


guess = input('Guess: ')

output = '