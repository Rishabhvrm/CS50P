class Student:
    # initialize method
    # initialize the contents of an object
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor","Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house



def main():
    student = get_student()

    # for list
    # if student[0] == "Padma":
    #     student[1] = "Ravenclaw"

    # for dictionary
    # if student["name"] == "Padma":
    #     student["house"] = "Ravenclaw"

    # print(f"{student.name} from {student.house}")


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
    # name = input("Name: ")
    # house = input("House: ")
    # return {"name": name, "house": house}

    # use class (introduction)
    # student = Student()
    # student.name = input("Name: ")
    # student.house = input("House: ")
    # return student

    # use constructor
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()


"""
Notes:

return multiple values
tuple - immutable, similar to list
Use a tuple when you don't want the values to get changed
Use a list when you may want to change the values
can change a tuple that contains list (can change list values)

Classes

# enough code to define a class
class Student:
    ...


instance methods:
    __init__(self)      # used to initialize the contents of an object from a class
    self - it gives us access to the object that was just created
    make parameters optional by None (house = None)

raise Errors


"""