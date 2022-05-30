email = input("What's your email? ").strip()

# eg 1
# 'pythonic' way of doing checking a character in a string
if "@" in email:
    print("Valid")
else:
    print("Invalid")

# eg 2
email2 = input("Okay, give me another email: ").strip()

username, domain = email2.split("@")

if (username) and ("." in domain):
    print("Valid")
else:
    print("Invalid")