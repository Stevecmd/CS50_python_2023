# Solution 1.
# name = str(input("What's your name? "))

# if name == "Harry":
#     print("Gryffindor")
# if name == "Hermione":
#     print("Gryffindor")
# if name == "Ron":
#     print("Gryffindor")
# if name == "Draco":
#     print("Slytherin")
# else:
#     print("Who? ")
#     print(f"{name} is an imposter! ")

# Solution 2.
# name = str(input("What's your name? "))

# if name == "Harry" or name == "Hermione" or name == "Ron":
#     print("Gryffindor")
# elif name == "Draco":
#     print("Slytherin")
# else:
#     print("Who? ")
#     print(f"{name} is an imposter! ")

# Solution 3
# name = str(input("What's your name? "))

# match name:
#     case "Harry":
#         print("Gryffindor")
#     case "Hermione":
#         print("Gryffindor")
#     case "Ron":
#         print("Gryffindor")
#     case "Draco":
#         print("Slytherin")
#     case _:
#         print(f"{name} is an imposter! ")

# Solution 4: NB: Only use in Python
name = str(input("What's your name? "))

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print(f"{name} is an imposter! ")