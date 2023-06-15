import random

def main():
    # input level
    level = get_level()
    strike, score, step = 0, 0, 0
    strike_counter = 0                                  # not necessary though

    for step in range(10):                              # run for 10 steps
        a, b = generate_integer(level)
        result = a + b
        for strike in range(3):                         # maximum three strikes for wrong answer
            try:
                guess = int(input(f'{a} + {b} = '))
                if guess != result:                     # print error and increase strike
                    print('EEE')
                    strike += 1
                else:
                    # correct guess, guess == result    # increase score and break out of strike loop
                    score += 1
                    break
            except ValueError:                          # user enters string/wrong input, increase strike
                print('EEE')
                strike += 1

        if strike == 3:
            # print(f'strike: {strike}')
            print(f'{a} + {b} = {result}')              # print correct answer after 3 wrong answers
            # strike_counter += 1
        # step += 1

    # print(f'strike_counter = {strike_counter}')
    print(f'Score = {score}')


# get levels. 1, 2, 3 only
# prompt again if user enters anything other than 1, 2, 3
def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level not in [1, 2, 3]:      # if user enters level other than 1, 2 or 3. raise ValueError
                raise ValueError
        except ValueError:
            pass                            # is user enters a string, prompt again
        else:
            return level

# generate tow random integers. Number of digits should be equal to input level
def generate_integer(level):
    # generate 1 digit random number
    if level == 1:
        a, b = random.randint(0, 9), random.randint(0, 9)
    # generate 2 digit random number
    elif level == 2:
        a, b = random.randint(10, 99), random.randint(10, 99)
    # generate 3 digit random number
    elif level == 3:
        a, b = random.randint(100, 999), random.randint(100, 999)
    return a, b

if __name__ == "__main__":
    main()