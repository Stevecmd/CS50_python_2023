# def main():
#     groceries()

# def groceries():
#     dict = {}

#     while True:
#         try:
#             item = input("Enter an item name (or 'quit' to stop): ").title()
#             if item in dict:
#                 dict[item] += 1
#             elif item.lower() == 'quit': break
#             else:
#                 dict[item] = 1

#         except EOFError:
#             print("\n")
#             for item, count in sorted(dict.items()):
#                 print(f"{count} {item.upper()}")
#             break

# main()

# def main():
#     groceries()

# def groceries():
#     dict = {}
#     item = input("Enter an item name (or 'quit' to stop): ")

#     while item.lower() != 'quit':
#         try:
#             if item in dict:
#                 dict[item] += 1
#             else:
#                 dict[item] = 1

#             item = input("Enter an item name (or 'quit' to stop): ").title()

#         except EOFError:
#             for item, count in sorted(dict.items()):
#                 print(f"{count} {item.upper()}")
#             break

# main()

# def main():
#     groceries()


# def groceries():
#     try:
#         grocery_dict = {}
#         item = input("Enter an item name (or 'quit' to stop): ").title()

#         while item.lower() != 'quit':
#             if item in grocery_dict:
#                 grocery_dict[item] += 1
#             else:
#                 grocery_dict[item] = 1

#         for item, count in sorted(grocery_dict.items()):
#             print(f"{count} {item}\n")
#     except EOFError:
#         print(f"{count} {item}\n")

# main()

def main():
    groceries()


def groceries():
    grocery_dict = {}
    try:
        #item = input("Enter an item name (or 'quit' to stop): ").title()
        item = input("").title()

        while item.lower() != 'quit':
            if item in grocery_dict:
                grocery_dict[item] += 1
            else:
                grocery_dict[item] = 1
            #item = input("Enter an item name (or 'quit' to stop): ").title()
            item = input("").title()

    except EOFError:
        pass

    finally:
        for item, count in sorted(grocery_dict.items()):
            print(f"{count} {item.upper()}")


main()
