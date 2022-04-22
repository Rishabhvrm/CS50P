x = float(input("What's x? "))
y = float(input("What's y? "))

# rounding off to nearest integer
z = round(x + y)

# add comma to the number, Eg: 1,000
print(f"{z:,}")


'''
checking if int() would take a string
a = input("Another input please: ")
b = int(a)
print(b)
'''