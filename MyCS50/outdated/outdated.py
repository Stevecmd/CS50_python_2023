# def main():
#     dates()

# def dates():
#     date_list = [
#     "January",
#     "February",
#     "March",
#     "April",
#     "May",
#     "June",
#     "July",
#     "August",
#     "September",
#     "October",
#     "November",
#     "December"
# ]

#     try:
#         item = input("Enter a date (or 'quit' to stop): ").date()

#         while item.lower() != 'quit':
#             if item in grocery_dict:
#                 grocery_dict[item] += 1
#             else:
#                 grocery_dict[item] = 1
#             item = input("").title()

#     except EOFError:
#         pass




# main()


# def ask_for_date():
#     while True:
#         date_str = input("Please enter a date in the ISO 8601 format (YYYY-MM-DD): ")
#         date_parts = date_str.split("-")

#         if len(date_parts) != 3:
#             print("That's not a valid date. Please try again.")
#             continue

#         year, month, day = date_parts
#         if len(year) == 4 and year.isdigit() and len(month) == 2 and month.isdigit() and 1 <= int(month) <= 12 and len(day) == 2 and day.isdigit() and 1 <= int(day) <= 31:
#             print(f"The date you entered is: {date_str}")
#             break
#         else:
#             print("That's not a valid date. Please try again.")

# ask_for_date()


# def format_date():
#     month_names = [
#         "January",
#         "February",
#         "March",
#         "April",
#         "May",
#         "June",
#         "July",
#         "August",
#         "September",
#         "October",
#         "November",
#         "December"
#     ]

#     while True:
#         date_str = input("Please enter a date in 'M/D/YYYY' or 'Month D, YYYY' format: ")

#         # Check if date is in 'M/D/YYYY' format
#         if "/" in date_str:
#             parts = date_str.split("/")
#             if len(parts) == 3 and parts[0].isdigit() and parts[1].isdigit() and parts[2].isdigit():
#                 month = parts[0].zfill(2) # Add leading zero if needed
#                 day = parts[1].zfill(2) # Add leading zero if needed
#                 year = parts[2]
#                 if 1 <= int(month) <= 12 and 1 <= int(day) <= 31 and len(year) == 4:
#                     print(f"The date you entered is: {year}-{month}-{day}")
#                     break

#         # Check if date is in 'Month D, YYYY' format
#         elif ", " in date_str:
#             parts = date_str.split(", ")
#             if len(parts) == 2 and parts[1].isdigit() and len(parts[1]) == 4:
#                 month_day = parts[0].split(" ")
#                 if len(month_day) == 2 and month_day[0] in month_names and month_day[1].isdigit():
#                     month = str(month_names.index(month_day[0]) + 1).zfill(2) # Convert month name to number
#                     day = month_day[1].zfill(2) # Add leading zero if needed
#                     year = parts[1]
#                     print(f"The date you entered is: {year}-{month}-{day}")
#                     break

#         print("That's not a valid date. Please try again.")

# format_date()

# def format_date():
#     month_names = [
#         "January",
#         "February",
#         "March",
#         "April",
#         "May",
#         "June",
#         "July",
#         "August",
#         "September",
#         "October",
#         "November",
#         "December"
#     ]

#     while True:
#         try:
#             date_str = input("Date: ")

#             # Check if date is in 'M/D/YYYY' format
#             if "/" in date_str:
#                 parts = date_str.split("/")
#                 if len(parts) == 3 and parts[0].isdigit() and parts[1].isdigit() and parts[2].isdigit():
#                     month = parts[0].zfill(2) # Add leading zero if needed
#                     day = parts[1].zfill(2) # Add leading zero if needed
#                     year = parts[2]
#                     if 1 <= int(month) <= 12 and 1 <= int(day) <= 31 and len(year) == 4:
#                         print(f"{year}-{month}-{day}")
#                         break

#             # Check if date is in 'Month D, YYYY' format
#             elif ", " in date_str:
#                 parts = date_str.split(", ")
#                 if len(parts) == 2 and parts[1].isdigit() and len(parts[1]) == 4:
#                     month_day = parts[0].split(" ")
#                     if len(month_day) == 2 and month_day[0] in month_names and month_day[1].isdigit():
#                         month = str(month_names.index(month_day[0]) + 1).zfill(2) # Convert month name to number
#                         day = month_day[1].zfill(2) # Add leading zero if needed
#                         year = parts[1]
#                         print(f"{year}-{month}-{day}")
#                         break

#         except EOFError:
#             pass

# format_date()


def format_date():
    month_names = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    while True:
        try:
            date_str = input("Date: ").strip() # strip removes leading and trailing whitespace as per tests

            # Check if date is in the format 'M/D/YYYY'
            # 1st check for dates formatted with '/'
            if "/" in date_str:
                parts = date_str.split("/") # Splitting each / as a separate part
                if len(parts) == 3 and parts[0].isdigit() and parts[1].isdigit() and parts[2].isdigit(): # Checking if all parts contain digits
                    month = parts[0].zfill(2) # Add leading zero if needed
                    day = parts[1].zfill(2) # Add leading zero if needed
                    year = parts[2]
                    if 1 <= int(month) <= 12 and 1 <= int(day) <= 31 and len(year) == 4:
                        print(f"{year}-{month}-{day}")
                        break

            # Check if date is in 'Month, Day, YYYY' format
            # 1st check for dates formatted with ','
            elif ", " in date_str:
                parts = date_str.split(", ") # Splitting each , as a separate part
                if len(parts) == 2 and parts[1].isdigit() and len(parts[1]) == 4:
                    month_day = parts[0].split(" ")
                    if len(month_day) == 2 and month_day[0] in month_names and month_day[1].isdigit() and 1 <= int(month_day[1]) <= 31:
                        month = str(month_names.index(month_day[0]) + 1).zfill(2) # Convert month name to number
                        day = month_day[1].zfill(2) # Add leading zero if needed
                        year = parts[1]
                        print(f"{year}-{month}-{day}")
                        break

        except EOFError:
            pass # pass means do nothing, typing ctrl + d or ctrl + z does nothing
        # pass - our code does not warn our user, but simply re-asks them our prompting question

format_date()

# Notes:
# The zfill() method in Python is a built-in method for strings that returns
# a new string from the original string left-padded with zeros (0) to a total of specified width.
# It's used to add leading zeros to a string, usually to make numbers align correctly.

# Computers tend to use ISO 8601, an international standard that prescribes that dates should be formatted
# in year-month-day (YYYY-MM-DD) order, no matter the country, formatting years with four digits, months with two digits,
# and days with two digits, “padding” each with leading zeroes as needed.