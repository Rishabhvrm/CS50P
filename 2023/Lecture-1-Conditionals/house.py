# match and case
# use '_' (underscore) for the default case

name = input("What's your name? ")

match name:
    case "Harry" | "Ron":
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
