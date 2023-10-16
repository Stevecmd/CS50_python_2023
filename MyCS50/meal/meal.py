# In meal.py, implement a program that prompts the user for a time and outputs whether it’s breakfast time,
# lunch time, or dinner time. If it’s not time for a meal, don’t output anything at all.
# Assume that the user’s input will be formatted in 24-hour time as #:## or ##:##.
# And assume that each meal’s time range is inclusive. For instance, whether it’s 7:00, 7:01, 7:59, or 8:00,
# or anytime in between, it’s time for breakfast.

# Structure your program per the below, wherein convert is a function (that can be called by main)
# that converts time, a str in 24-hour format, to the corresponding number of hours as a float.
# For instance, given a time like "7:30" (i.e., 7 hours and 30 minutes), convert should return 7.5 (i.e., 7.5 hours).



def main():
    time = input("What is the time? ").strip()
    meal_time(convert(time))


def convert(time):
    split_time = time.split(":")
    hours = int(split_time[0])
    minutes = int(split_time[1])
    return hours + (minutes / 60)

def meal_time(time):
    if 7 <= time < 9:
        print("breakfast time")
    elif 12 <= time < 14:
        print("lunch time")
    elif 18 <= time < 21:
        print("dinner time")

if __name__ == "__main__":
    main()

# if __name__ == "__main__": main() is a common Python idiom.
# When a Python file is run directly (not imported as a module),
# the special variable __name__ is set to "__main__". So if __name__ == "__main__": main()
# means "if this file is being run directly, call the main() function". If the file is
# imported as a module, __name__ will be the name of the module, so main() won't be called.
# This allows you to have code in your file that is only run when the file is executed directly,
# not when it's imported as a module.