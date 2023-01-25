# take user input
user_input = input("Expression: ").strip().split()

# initialize x, y and z, convert x and z to int
x, y, z = int(user_input[0]), user_input[1], int(user_input[2])

# if y == /, then z can't be 0, raise an error
if y == '/' and z == 0:
    raise ZeroDivisionError('division by zero is not allowed')

# initialize ans
ans = 0.0

# use match case for each operator
match y:
    case '+':
        ans = x + z
    case '-':
        ans = x - z
    case '*':
        ans = x * z
    case '/':
        ans = x / z

# final output
print(float(ans))