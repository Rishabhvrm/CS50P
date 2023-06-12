import inflect

names = []

# keep prompting the user until CTRL + D
while True:
    try:
        name = input("Names: ").strip()
    except EOFError:
        break
    else:
        names.append(name)

# join words into a list using inflect
p = inflect.engine()
print()
print(p.join(names))