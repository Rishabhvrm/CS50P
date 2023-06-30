# clean up or format user input data

name = input("What's your name? ").strip()
if "," in name:
    last, first = name.split(", ")
print(f"hello, {first} {last}")