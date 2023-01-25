# making this file to demonstrate how to keep prompting user for till a condition is satisfied

# keep asking the user to provide n until it's a positive number
# i.e. keep repeating the question if user provides a negative number

while True:
    n = int(input("What's n? "))
    # break out as soon as you get a positive number
    if n > 0:
        break

for _ in range(n):
    print("meow")