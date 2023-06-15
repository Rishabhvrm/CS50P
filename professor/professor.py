import random

def main():

    level = get_level()
    print(level)
    a, b = generate_integer(level)
    result = a + b

    strike = 0
    score = 0

    for strike in range(3):
        guess = int(input(f'{a} + {b} = '))
        try:
            if guess != result:
            print('EEE')
            strike += 1
        except ValueError:
            
        else:
            score += 1
            break


# get levels. 1, 2, 3 only
# prompt again if user enters anything other than 1, 2, 3
def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            pass
        else:
            if level > 3 or level < 1:
                pass
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