x = int(input("What's x? "))
y = int(input("What's y? "))


# if, elif, else
if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")
else:
    print("x is equal to y")

# or
if x > y or x < y:
    print("x is not equal to y")
else:
    print("x is equal to y")