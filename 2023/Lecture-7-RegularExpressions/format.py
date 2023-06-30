# clean up or format user input data

import re

name = input("What's your name? ").strip()
# matches = re.search(r"^.+, .+$", name)
# not grouping by using (), we want a return value, we want to capture something
if matches := re.search(r"^(.+), *(.+)$", name):                                    # i.e. we found something, matches is not empty
    last = matches.group(1)
    first = matches.group(2)
    name = f"{first} {last}"
print(f"hello, {name}")


"""

NOTES:

we can extract info from re, using paranthesis OR grouping
re.search() returns whatever matches in the given string with the pattern
get a return value for when grouped
use it using matches.groups()    # as seen in above code

whatever matches in paranthesis, can be returned
(?:...) don't capture, just group

walrus operator :=
assign a return value, ask a boolean question (if, elif), both thing at the same time

"""