email = input("What's your email? ").strip()


# 'pythonic' way of doing checking a character in a string
if "@" in email:
    print("Valid")
else:
    print("Invalid")