user_input = input("camelCase: " )

# split the words ?
for c in user_input:
    if c.isupper():
        print("_" + c.lower(), end = "")
    else:
        print(c, end = "")
print()


# lower the words

# add an underscore btw the words and output