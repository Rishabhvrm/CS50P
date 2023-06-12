import random

# looping until user enters integer
while True:
    try:
        n = int(input('Level: '))
    except ValueError:
        pass
    else:
        number = random.randint(1,n)        # choose a random number inclusive of the parameters
        break

# looping until user enter integer
while True:
    try:
        guess = int(input('Guess: '))
    except ValueError:
        pass
    else:
        if guess == number:
            print('Just right!')
            break
        print('Too large!' if guess > number else 'Too small!')     # using ternary with print