# cleaner version of 1.student.py

class Student:

    # initialize method
    # initialize the contents of an object
    def __init__(self, name, house):
        self.name = name
        self.house = house

    # used to print a object
    def __str__(self):
        return f"{self.name} is from {self.house}"

    # class method
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    # Getter
    @property
    def house(self):
        return self._house      # variable can't have same name as the function
        # it will return the value set by setter function

    # Setter
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor","Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house     # variable can't have same name as the function



def main():
    student = get_student()
    student._house = "privet"
    print(student)

if __name__ == "__main__":
    main()


"""
Notes:


"""