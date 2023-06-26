count = 0

with open('sample.py') as file:
    for line in file:
        if not line.startswith('#') and line.strip() != "":
            print('start' + line + 'end')
            count += 1

print(count)