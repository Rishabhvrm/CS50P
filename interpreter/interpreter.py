# take user input
user_input = input().strip().split()

# initialize x, y and z
x, y, z = int(user_input[0]), user_input[1], int(user_input[2])

match y:
    case '+':
        ans = x + y
    case '-':
        ans = x - y
    case '*':
        ans = x * y
    case '/':
        ans = x / y

# if y == /, then z can't be 0
ans = xyz
print(ans)