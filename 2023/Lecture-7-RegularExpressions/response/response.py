from validator_collection import validators

def main():
    print(validate(input("What's your email address? ")))

def validate(email):
    print(validators.email(email))

if __name__ == "__main__":
    main()