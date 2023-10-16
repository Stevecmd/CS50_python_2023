# # Solution 1
# import random

# class Hat:
#     def __init__(self):
#         self.houses = ["Gryffindor","Slytherin","Hufflepuff","Raven Claw"]

#     def sort(self, name):
#         print(name, "is in", random.choice(self.houses))


# hat = Hat()
# hat.sort("Harry")

# Solution 2
import random

class Hat:
    # def __init__(self):
    houses = ["Gryffindor","Slytherin","Hufflepuff","Raven Claw"]

    @classmethod
    def sort(cls, name): # cls is class
        print(name, "is in", random.choice(cls.houses))

Hat.sort("Harry")