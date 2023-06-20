def main():
    greeting = input("Greeting: ")
    print(f'${value(greeting.lower())}')

def value(greeting):
    if greeting[0] == "hello":
        return 0
    elif greeting[0].startswith() == "h":
        return 20
    else: return 100

if __name__ == "__main__":
    main()