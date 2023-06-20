def main():
    plate = input("Plate: ")
    print("Valid" if is_valid(plate) else "Invalid")

def is_valid(s):
    valid = False
    # check conditions
    if max_min_char_length(s) and starts_with_two_letters(s) and check_ends_with_num(s) and no_period(s):
        valid = True
    return valid

# length of chars in string must be btw [2,6]
def max_min_char_length(s):
    # check the length of chars in string
    chars = [char for char in s if char in string.ascii_letters]
    return 2 <= len(chars) <= 6

# https://docs.python.org/3/library/string.html
def starts_with_two_letters(s):
    # check if first 2 letters are ascii letters
    return (s[0] in string.ascii_letters and s[1] in string.ascii_letters)

# https://docs.python.org/3/library/string.html
def no_period(s):
    # check for punctation in s
    for p in string.punctuation:
        if p in s:
            return False

    # check for whitespace in s
    for p in string.whitespace:
        if p in s:
            return False
    return True

# string should end with a number not a char
def check_ends_with_num(s):
    flag, zero_flag = True, True
    l, count_digits, count_char = len(s), 0, 0

    for i in range(l):
        if s[i].isdigit():
            count_digits += 1

            # check if next element encountered after a digit is also digit
            # check current index is not the end of string
            # check if element in next index is digit or not (if it's not a digit, set flag = False)
            if i+1 is not l and not s[i+1].isdigit():
                flag = False

            # should be inside first 'if' else i would be increased
            # first digit can't be 0
            if count_digits == 1 and s[i] == '0':
                zero_flag = False

    # return true if both condtions are met else false
    return flag and zero_flag

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