class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing Name")
        self.name = name

# class Student:
#     def __init__(self, name, house):
#         self.name = name
#         self.house = house

# class Professor:
#     def __init__(self, name, subject):
#         self.name = name
#         self.subject = subject

class Student(Wizard):
    def __init__(self,name, house):
        super().__init__(name)
        self.house = house

class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Defense Against the Dark Arts")

"""

both student and professor have name
better to define a class wizard which will have common attributes like name into it
and then student and professor can inherit the wizard class

class Child inherits from class Parent
 definition => class Child(Parent):
 super() => access the parent class
 super().__init__ => access parent's class __init__() method

 """