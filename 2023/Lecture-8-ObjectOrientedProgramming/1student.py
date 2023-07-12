def main():
    student = get_student()

    # if student[0] == "Padma":
    #     student[1] = "Ravenclaw"

    if student["name"] == "Padma":
        student["house"] = "Ravenclaw"

    print(f"{student['name']} from {student['house']}")


def get_student():
    # name = input("Name: ")
    # house = input("House: ")
    # return name, house          # we're actually returning one tuple, not two values
    # return (name, house)        # same as above
    # return [name, house]        # return a list bcz we want to change the value

    # student = {}
    # student["name"] = input("Name: ")
    # student["house"] = input("House: ")
    # return student

    # same thing as above
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}

if __name__ == "__main__":
    main()


"""
Notes:

return multiple values
tuple - immutable, similar to list
Use a tuple when you don't want the values to get changed
Use a list when you may want to change the values



"""