i = 0

while i < 3:
    print("meow")
    i += 1

# list
for i in [0, 1, 2]:
    print("woof")

# range function in python
for _ in range(5):
    print("moo")

# multiply by a number to print a text that many times
print("sample\n" * 3, end = "")

print("new topic now")

# pythonic way or a convention to take user input, until user gives valid value
while True:
    n = int(input("What's x? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")