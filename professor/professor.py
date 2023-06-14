import random

def main():
    level = get_level()
    print(level)
    int = generate_integer(level)
    

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


def generate_integer():
    pass

if __name__ == "__main__":
    main()