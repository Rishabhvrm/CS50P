names = []

for _ in range(3):
    names.append(input("What's your name? "))

print(names)

for name in sorted(names):
    print(f"hello, {name}")

print(names)