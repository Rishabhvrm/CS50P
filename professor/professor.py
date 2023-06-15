import random

def main():
    # input level
    level = get_level()
    strike = 0
    score = 0
    step = 0
    strike_counter = 0

    # run for 10 steps
    for step in range(10):
        a, b = generate_integer(level)
        result = a + b
        for strike in range(3):
            try:
                guess = int(input(f'{a} + {b} = '))
                if guess != result:
                    print('EEE')
                    strike += 1
                else:
                    # guess is equal to result
                    score += 1
                    break
            except ValueError:
                print('EEE')
                strike += 1
        if strike == 3:
            print(f'strike: {strike}')
            print(f'{a} + {b} = {result}')
            strike_counter += 1
        step += 1

    # print(f'strike_counter = {strike_counter}')
    print(f'Score = {score}')


# get levels. 1, 2, 3 only
# prompt again if user enters anything other than 1, 2, 3
def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level not in [1, 2, 3]:      # if user enters level other than 1, 2 or 3
                raise ValueError
        except ValueError:
            pass                            # is user enters a string
        else:
            return level


def generate_integer(level):
    if level == 1:
        a, b = random.randint(0, 9), random.randint(0, 9)
    elif level == 2:
        a, b = random.randint(10, 99), random.randint(10, 99)
    elif level == 3:
        a, b = random.randint(100, 999), random.randint(100, 999)
    return a, b

if __name__ == "__main__":
    main()