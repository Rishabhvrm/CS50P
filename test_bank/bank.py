def main():
    greeting = input("Greeting: ")
    print(f'${value(greeting.lower())}')

def value(greeting):
    if greeting == "hello":
        return 100
    elif greeting[0] == "h":
        return 20
    else: return 0

if __name__ == "__main__":
    main()