count = 0

with open('sample.py') as file:
    for line in file:
        if not line.startswith('#') and line.strip != "":
            print("yep")
            count += 1

print(count)