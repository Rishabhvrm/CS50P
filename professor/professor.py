import random

def main():
    level = get_level()
    print(level)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError or level > 3 or level < 0:
            print('trueeeeee')
            pass
        else:
            return level


def generate_integer():
    pass

if __name__ == "__main__":
    main()