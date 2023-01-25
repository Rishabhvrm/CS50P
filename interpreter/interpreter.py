# take user input
user_input = input().strip().split()

# initialize x, y and z
x, y, z = int(user_input[0]), user_input[1], int(user_input[2])

ans = 0.0

match y:
    case '+':
        ans = x + y
    case '-':
        ans = x - y
    case '*':
        ans = x * y
    case '/':
        if z != 0:
            ans = x / y     # if y == /, then z can't be 0

print(ans)