# take user input
greeting = input("Greeting: ").strip().lower()

# use startswith() method to check the conditions
if greeting.startswith("hello"):
    print("$0")
elif greeting.startswith("h"):
    print("$20")
else:
    print("$100")
