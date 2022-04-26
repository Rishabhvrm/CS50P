x = float(input("What's x? "))
y = float(input("What's y? "))

# rounding off to nearest integer
z = round(x + y)

# add comma to the number, Eg: 1,000
# f string, a string where you could pass values in {}
print(f"value with comma: {z:,}")

# division
a = float(input("What's a? "))
b = float(input("What's b? "))

# rounding off to nearest integer
c = round(a / b, 3)
print(c)

d = a / b
print(f"{d:.2f}")

'''
checking if int() would take a string
a = input("Another input please: ")
b = int(a)
print(b)
'''