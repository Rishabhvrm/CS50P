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
    def __init__(house):
        self.house = house



"""

both student and professor have name
better to define a class wizard which will have common attributes like name into it
and then student and professor can inherit the wizard class

class Child inherits from class Parent
 - definition => class Child(Parent):

 """