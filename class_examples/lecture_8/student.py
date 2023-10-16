# Solution 1
# def main():
#     student = get_student()
#     if student["name"] == "Steve":
#         student["house"] == "HufflePuff"
#         print(f"{student['name']} from {student['house']}")

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return {"name": name, "house": house}

# if __name__ == "__main__":
#     main()

# Solution 2
# class Student:
#     def __init__(self, name='', house=''):
#         self.name = name
#         self.house = house

# def main():
#     student = get_student()
#     print(f"{student.name} from {student.house}")

# def get_student():
#     student = Student() # Creating an object / instance from a class
#     student.name = input("Name: ")
#     student.house = input("House: ")
#     return student

# if __name__ == "__main__":
#     main()

#

# Student class
# student function

# # Solution 4
# class Student:
#     def __init__(self, name='', house=''): # Initializing the contents of objects
#         self.name = name # self gives access to the current variable
#         self.house = house

# def main():
#     student = get_student()
#     print(f"{student.name} from {student.house}")

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     student = Student(name, house) # This is a constructor call
#     return student

# if __name__ == "__main__":
#     main()


# # Solution 5
# class Student:
#     def __init__(self, name, house,patronus): # Initializing the contents of objects
#         if not name:
#             raise ValueError("Missing name")
#         if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
#             raise ValueError("Invalid House")
#         self.name = name # self gives access to the current variable
#         self.house = house
#         self.patronus = patronus
#     def __str__(self):
#         return f"{self.name} from {self.house}"

#     def charm(self):
#         match self.patronus:
#             case "Stag":
#                 return "👣"
#             case "Otter":
#                 return "👨🏻‍🚀"
#             case "Jack Russel terrier":
#                 return "👩🏼‍🎓"
#             case _:
#                 return "🛌🏼"

# def main():
#     student = get_student()
#     print("Expecto patronum!")
#     # print(f"{student.name} from {student.house}")
#     print(student.charm())

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     patronus = input("Patronus: ")
#     student = Student(name, house, patronus) # This is a constructor call
#     return student

# if __name__ == "__main__":
#     main()


# # # Solution 6
# # _ - variables named with an underscore shouldnt be touched
# # _ - variables named with double underscore shouldnt be touched at all!!!

# class Student:
#     def __init__(self, name, house): # Initializing the contents of objects
#         self.name = name # self gives access to the current variable
#         self.house = house

#     def __str__(self):
#         return f"{self.name} from {self.house}"

#     @property
#     def name(self):
#         return self._name

#     @name.setter
#     def name(self, name):
#         if not name:
#             raise ValueError("Missing name")
#         self._name = name

#     #Getter
#     @property
#     def house(self):
#         return self._house

#     #Setter
#     @house.setter
#     def house(self, house):
#         if house not in ["Gryffindor","Slytherin","Hufflepuff","Ravenclaw"]:
#             raise ValueError("Invalid house")
#         self._house = house

# def main():
#     student = get_student()
#     print(student)

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return Student(name, house) # This is a constructor call


# if __name__ == "__main__":
#     main()


# # Solution 7
# _ - variables named with an underscore shouldnt be touched
# _ - variables named with double underscore shouldnt be touched at all!!!

class Student:
    def __init__(self, name, house): # Initializing the contents of objects
        self.name = name # self gives access to the current variable
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)

def main():
    student = Student.get()
    print(student)

if __name__ == "__main__":
    main()
