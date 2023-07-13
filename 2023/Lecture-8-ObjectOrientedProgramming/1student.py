class Student:

    # initialize method
    # initialize the contents of an object
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        self.name = name
        self.house = house

    # used to print a object
    def __str__(self):
        return f"{self.name} is from {self.house}"

    def charm(self):
        match self.patronus:
            case "Stag":
                return "horse"
            case "Otter":
                return "sea-otter"
            case "Jack Russell terrier":
                return "dog"
            case _:
                return "/"


    # Getter
    @property
    def house(self):
        return self._house      # variable can't have same name as the function

    # Setter
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor","Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house     # variable can't have same name as the function



def main():
    student = get_student()
    student.house = "private"
    # for list
    # if student[0] == "Padma":
    #     student[1] = "Ravenclaw"

    # for dictionary
    # if student["name"] == "Padma":
    #     student["house"] = "Ravenclaw"

    # print(f"{student.name} from {student.house}")
    print(student)


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
    # patronus = input("Patronus: ")
    # return Student(name, house, patronus)
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


Classes:
# enough code to define a class
class Student:
    ...

instance methods:
    __init__(self)      # used to initialize the contents of an object from a class
    self - it gives us access to the object that was just created
    self should be present in every method in a class which will reference to the current object
    make parameters optional by None (house = None)
    __str__ - more for users
    __repr__ - more for developer's eye

raise Errors

we can still change the values of attributes once their values has been assigned
properties
decorators - functions that modify the behaviour of other functions
@property - getter
@getter_name.setter - setter

if setter is there then we can't use student.house = "abc"

function and variable can't have same name
put an underscore to differentiate


"""