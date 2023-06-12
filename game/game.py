import random

n = int(input('Level: '))

# choose a random number inclusive of the parameters
number = random.randint(1,n)
print(number)


guess = int(input('Guess: '))

output = 'just right' if guess == number else 'large' if guess > number else 'small'

print(output)