import re

def main():
    print(convert(input("Hours: ")))

def convert(time):
    # allowed input - 9:00 AM to 5:00 PM
    if matches := re.search(r"^(\d{1,2}):(\d{1,2}) (AM|PM) to (\d{1,2}):(\d{1,2}) (AM|PM)$", time):
        # print('Yayy')
        hour, minute, time_indicator = matches.group(1), matches.group(2), matches.group(3)
        start = convert_to_military_time(time_indicator, hour, minute)

        hour, minute, time_indicator = matches.group(4), matches.group(5), matches.group(6)
        end = convert_to_military_time(time_indicator, hour, minute)

        return f"{start} to {end}"

    # allowed input - 9 AM to 5 PM
    elif matches := re.search(r"^(\d{1,2}) (AM|PM) to (\d{1,2}) (AM|PM)$", time):
        # print('Nayy')
        hour, time_indicator = matches.group(1), matches.group(2)
        start = convert_to_military_time(time_indicator, hour)

        hour, time_indicator = matches.group(3), matches.group(4)
        end = convert_to_military_time(time_indicator, hour)

        return f"{start} to {end}"

    else:
        raise ValueError


def convert_to_military_time(time_indicator, h, m="00"):
    # validate time
    validate_time(h,m)

    # add 12 for every case except 12
    # don't need 24:00 for 12 PM
    if time_indicator == "PM" and h != "12":
        h = str(int(h) + 12)

    # 12 AM is 00
    if time_indicator == "AM" and h == "12":
        h = "00"

    # 9 -> 09
    if len(h) == 1: h = f"0{h}"
    return f"{h}:{m}"

def validate_time(h,m):
    if not 0 <= int(h) <= 12 or not 0 <= int(m) <= 59:
        raise ValueError


if __name__ == "__main__":
    main()



"""
PSET-7 Working 9 to 5

# https://cs50.harvard.edu/python/2022/psets/7/working/

Whereas most countries use a 24-hour clock, the United States tends to use a 12-hour clock. Accordingly, instead of “09:00 to 17:00”, many Americans would say they work “9:00 AM to 5:00 PM” (or “9 AM to 5 PM”), wherein “AM” is an abbreviation for “ante meridiem” and “PM” is an abbreviation for “post meridiem”, wherein “meridiem” means midday (i.e., noon).

Conversion Table
In a file called working.py, implement a function called convert that expects a str in either of the 12-hour formats below and returns the corresponding str in 24-hour format (i.e., 9:00 to 17:00). Expect that AM and PM will be capitalized (with no periods therein) and that there will be a space before each. Assume that these times are representative of actual times, not necessarily 9:00 AM and 5:00 PM specifically.

9:00 AM to 5:00 PM
9 AM to 5 PM
Raise a ValueError instead if the input to convert is not in either of those formats or if either time is invalid (e.g., 12:60 AM, 13:00 PM, etc.). But do not assume that someone’s hours will start ante meridiem and end post meridiem; someone might work late and even long hours (e.g., 5:00 PM to 9:00 AM).

Structure working.py as follows, wherein you’re welcome to modify main and/or implement other functions as you see fit, but you may not import any other libraries. You’re welcome, but not required, to use re and/or sys.

import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    ...


...


if __name__ == "__main__":
    main()
Either before or after you implement convert in working.py, additionally implement, in a file called test_working.py, three or more functions that collectively test your implementation of convert thoroughly, each of whose names should begin with test_ so that you can execute your tests with:

pytest test_working.py
Hints
Recall that the re module comes with quite a few functions, per docs.python.org/3/library/re.html, including search.
Recall that regular expressions support quite a few special characters, per docs.python.org/3/library/re.html#regular-expression-syntax.
Because backslashes in regular expressions could be mistaken for escape sequences (like \n), best to use Python’s raw string notation for regular expression patterns, else pytest will warn with DeprecationWarning: invalid escape sequence. Just as format strings are prefixed with f, so are raw strings prefixed with r. For instance, instead of "harvard\.edu", use r"harvard\.edu".
Note that re.search, if passed a pattern with “capturing groups” (i.e., parentheses), returns a “match object,” per docs.python.org/3/library/re.html#match-objects, wherein matches are 1-indexed, which you can access individually with group, per docs.python.org/3/library/re.html#re.Match.group, or collectively with groups, per docs.python.org/3/library/re.html#re.Match.groups.
Note that you can format an int with leading zeroes with code like
print(f"{n:02}")
wherein, if n is a single digit, it will be prefixed with one 0, per docs.python.org/3/library/string.html#format-string-syntax.

"""