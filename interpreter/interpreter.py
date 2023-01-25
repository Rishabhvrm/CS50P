# take user input
user_input = input("Expression: ").strip().split()

# initialize x, y and z
x, y, z = int(user_input[0]), user_input[1], int(user_input[2])

ans = 0.0

match y:
    case '+':
        ans = x + z
    case '-':
        ans = x - z
    case '*':
        ans = x * z
    case '/':
        if z != 0:
            ans = x / z     # if y == /, then z can't be 0

print(float(ans))