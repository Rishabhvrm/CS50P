def main():
    greeting = input("Greeting: ")
    print(f'${value(greeting.lower())}')

def value(greeting):
    if greeting.startswith("hello"):
        print(greeting)
        return 0
    elif greeting.startswith("h"):
        return 20
    else: return 100

if __name__ == "__main__":
    main()