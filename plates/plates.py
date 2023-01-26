import string

def main():
    plate = input("Plate: ")
    print("Valid" if is_valid(plate) else ".")

def is_valid(s):
    valid = False

    #starts_with_two_letters(s)
    #max_min_length(s)
    #num_at_end(s)
    #first_num_zero(s)
    no_period(s)

    #if (a and b and c and d):
    #    valid = True

    return valid

def starts_with_two_letters(s):
        print (s[0] in string.ascii_letters and s[1] in string.ascii_letters)

# https://docs.python.org/3/library/string.html
def no_period(s):
    print(string.punctuation)
    print(string.punctuation not in s)
    print(string.whitespace)
    print(string.whitespace not in s)
    print (string.punctuation not in s and string.whitespace not in s)

main()

