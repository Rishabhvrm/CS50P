count = 0

with open('sample.py') as file:
    for line in file:
        if line.startswith('#') or line.strip != "":
            print('start' + line + 'end')
            count += 1

print(count)