from validator_collection import validators, errors

def main():
    print(validate(input("What's your email address? ")))

def validate(email):
    try:
        return "Valid" if validators.email(email) else "Invalid"
    except errors.EmptyValueError:
        return "Invalid"
    except errors.InvalidEmailError:
        return "Invalid"


if __name__ == "__main__":
    main()