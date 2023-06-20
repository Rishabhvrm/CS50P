def main():
    plate = input("Plate: ")
    print("Valid" if is_valid(plate) else "False")

def is_valid(plate):
    return False



if __name__ == "__main__":
    main()


# -------------------------------------------------------------------------------------------------------------------
# Re-requesting a Vanity Plate

# In a file called plates.py, reimplement Vanity Plates from Problem Set 2, restructuring your code per the below, wherein is_valid still expects a str as input and returns True if that str meets all requirements and False if it does not, but main is only called if the value of __name__ is "__main__":

# def main():
#     ...


# def is_valid(s):
#     ...


# if __name__ == "__main__":
#     main()
# Then, in a file called test_plates.py, implement four or more functions that collectively test your implementation of is_valid thoroughly, each of whose names should begin with test_ so that you can execute your tests with:

# pytest test_plates.py

# -------------------------------------------------------------------------------------------------------------------