import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    # 0 or 1, 1 to 9, 1 to 9 (0-199) OR 2, 0 to 4, 0 to 9 (200-249) OR 25,0-5 (250-255)
    regex = "([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])"
    return True if re.search(rf"^{regex}\.{regex}\.{regex}\.{regex}$", ip) else False

if __name__ == "__main__":
    main()



# PSET 7
# https://cs50.harvard.edu/python/2022/psets/7/numb3rs/
"""
An IPv4 address is a numeric identifier that a device (or, on TV, hacker) uses to communicate on the internet, akin to a postal address in the real world, typically formatted in dot-decimal notation as #.#.#.#. But each # should be a number between 0 and 255, inclusive. Suffice it to say 275 is not in that range! If only NUMB3RS had validated the address in that scene!

In a file called numb3rs.py, implement a function called validate that expects an IPv4 address as input as a str and then returns True or False, respectively, if that input is a valid IPv4 address or not.

Structure numb3rs.py as follows, wherein you’re welcome to modify main and/or implement other functions as you see fit, but you may not import any other libraries. You’re welcome, but not required, to use re and/or sys.

import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    ...


...


if __name__ == "__main__":
    main()
Either before or after you implement validate in numb3rs.py, additionally implement, in a file called test_numb3rs.py, two or more functions that collectively test your implementation of validate thoroughly, each of whose names should begin with test_ so that you can execute your tests with:

pytest test_numb3rs.py
Hints
Recall that the re module comes with quite a few functions, per docs.python.org/3/library/re.html, including search.
Recall that regular expressions support quite a few special characters, per docs.python.org/3/library/re.html#regular-expression-syntax.
Because backslashes in regular expressions could be mistaken for escape sequences (like \n), best to use Python’s raw string notation for regular expression patterns, else pytest will warn with DeprecationWarning: invalid escape sequence. Just as format strings are prefixed with f, so are raw strings prefixed with r. For instance, instead of "harvard\.edu", use r"harvard\.edu".
Note that re.search, if passed a pattern with “capturing groups” (i.e., parentheses), returns a “match object,” per docs.python.org/3/library/re.html#match-objects, wherein matches are 1-indexed, which you can access individually with group, per docs.python.org/3/library/re.html#re.Match.group, or collectively with groups, per docs.python.org/3/library/re.html#re.Match.groups.

"""