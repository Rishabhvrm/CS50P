# take user input
user_input = input("camelCase: " )

# check if a character is upper or lower
# if lower then print as is
# if upper then convert to lower and prepend with underscore
# set 'end' = "" in print thereby overriding the default '/n' new-line
for c in user_input:
    if c.isupper():
        print("_" + c.lower(), end = "")
    else:
        print(c, end = "")

# move the cursor to a new line
print()