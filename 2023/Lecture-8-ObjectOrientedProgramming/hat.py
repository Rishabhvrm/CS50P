# Class Method
import random

class Hat:
    # def __init__(self):
    #     self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))

# before class method
# hat = Hat()
# hat.sort("Harry")

# after class method
Hat.sort("Harry")

"""
Class Method

@classmethod
    - this method is not an instance method, doesn't have access to 'self'
    - if there are no objects of that class
    - when class is just a container for data and functionality that are somehow related
    - pass 'cls' in the method
    - no need to instantiate the class

class variable
    - eg: houses in above eg
    - share the same copy among all the objects

"""