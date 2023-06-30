email = input("What's your email? ").strip()



# username, domain = email.split("@")
# if username and domain.endswith(".edu"):          # 2 separate boolean expressions
#     print("Valid")
# else:
#     print("Invalid")

"""
re : regular expressions, patterns
validate
"""

import re

# .* - any character 0 or more times
# .+ - any character 1 or more times

# if re.search(".+@.+", email):                 # something before '@', something after
# if re.search("..*@..*.edu", email):           # same as above

# good practice to use r string for regex
# if re.search(r"..*@..*\.edu", email):         # adding 'r' for raw string, using \ to escape '.'
# if re.search(r"^.+@.+\.edu$", email):         # using ^ (start) and $ (end)
# if re.search(r"^.+@{1}+\.edu$", email):       # same as below
# if re.search(r"^[^@]+@[^@]+\.edu$", email):   # [^@]+ : here + means same, one or more of the things to the left
# if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):     # include alphabets, digits, underscore before and after '@'
# if re.search(r"^\w+@\w+\.edu$", email):        # using \w for [a-zA-Z0-9]
# if re.search(r"^\w+@\w+\.edu$", email, re.IGNORECASE):         # case insensitive version
# if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE): # valid for something like rishabh.v@bufflo.edu. \. means only allowed value is a dot
if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):   # using grouping (...) -> (\w+\.)? -> mean 1 or more word followed by a dot can be there once or not at all, because of '?'. \. means just a dot not anything else
    print("Valid")
else:
    print("Invalid")


"""
NOTES:

good practice to use r string for regex (raw string)

. any character except newline
* 0 or more repetitions (of the things to left)
+ 1 or more repetitions (of the things to left)
? 0 or 1 repetition
{m} m repetitions
{m,n} m-n repetitions

.* any character 0 or more times
.+ any character 1 or more times

raw string: This means that backslashes within the string are treated as literal backslashes and not as escape characters

^ matches start of string
$ matches end of string just before newline at end of string

[] set of characters
[^] complementing the set

[a-zA-Z0-9] represents only allow alphbets and digits. No separator needed in between a to z, A to Z and 0 to 9
\w known as 'word character'. Contains alphanumeric and underscore. Same as above

\W not a word character
\d decimal digit
\D not a decimal digit
\s whitespace characters
\S not a whitespace character

(com|edu|gov|net|org) here | = OR. Eg: re.search(r"^\w+@\w+\.(edu|org|gov)$", email)
(\w|\s) a word or a space. Similar to [a-zA-Z0-9_ ]
A|B either A or B
(...) a group
(?:...) non-capturing version

re flags:
    re.IGNORECASE : case insensitive
    re.MULTILINE : matches multiple lines
    re.DOTALL : . means any character and new line (usually dot means any character except newline)


re.match(pattern, string, flag)        no need for ^. Takes care of start.
re.fullmatch(pattern, string, flag)    no need for ^ or $. Takes care of start and end.


"""
