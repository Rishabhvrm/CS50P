import random

n = int(input('Level: '))

# choose a random number inclusive of the parameters
number = random.randint(1,n)
print(number)

while True:
    guess = int(input('Guess: '))

    if guess < number:
        print('Too small!')
    elif guess > number:
        print('Too large!')
    elif guess == number:
        print('Just right!')
        break

