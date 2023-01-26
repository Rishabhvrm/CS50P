import string

def main():
    plate = input("Plate: ")
    print("Valid" if is_valid(plate) else ".")

def is_valid(s):
    valid = False

    #print(starts_with_two_letters(s))
    #print(max_min_length(s))
    print(num_at_end(s))
    #first_num_zero(s)
    #print(no_period(s))

    #if (a and b and c and d):
    #    valid = True

    return valid

# https://docs.python.org/3/library/string.html
def starts_with_two_letters(s):
        # check if first 2 letters are ascii letters
        return (s[0] in string.ascii_letters and s[1] in string.ascii_letters)

# length of string must be btw [2,6]
def max_min_length(s):
    return 2 <= len(s) <= 6

def num_at_end(s):
    # if string has any digit at all
    if any(c.isdigit() for c in s):
        # if string has any digit at 2nd, 3rd, 4th or 5th index
        # check till last, all should be digits
        if (check_digit_till_last(s,2)
        or check_digit_till_last(s,3)
        or check_digit_till_last(s,4)
        or check_digit_till_last(s,5)):
            return True

def check_digit_till_last(s,i):
    if s[i].isdigit():
        for _ in s[i:-1]:
            if not _.isdigit():
                return False
    return True




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


main()

