from validator_collection import validators, errors

def main():
    print(validate(input("What's your email address? ")))

def validate(email):
    try:
        flag = validators.email(email)
    except errors.EmptyValueError:
        return "Invalid"
    except errors.InvalidEmailError:
        return "Invalid"
    else


if __name__ == "__main__":
    main()