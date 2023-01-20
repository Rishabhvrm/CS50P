# take user input
ans = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()

# check conditions
if ans == "forty two":
    print("Yes")
elif ans == "forty-two":
    print("Yes")
# use 42 as string for valid comparison
elif ans == "42":
    print("Yes")
else:
    print("No")