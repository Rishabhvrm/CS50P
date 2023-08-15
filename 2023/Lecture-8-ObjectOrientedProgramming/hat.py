# Class Method
import random

class Hat:
    def __init__(self):
        self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    def sort(self, name):
        print(name, "is in", random.choice(self.houses))

hat = Hat()
hat.sort("Harry")



"""
Class Method

@classmethod
    - this method is not an instance method, doesn't have access to 'self'
    - if there are no objects of that class
"""