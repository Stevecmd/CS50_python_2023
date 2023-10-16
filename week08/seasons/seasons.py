from datetime import date
import sys
import inflect

def minutes_since_birth(dob):
    today = date.today()
    days_difference = (today - dob).days
    minutes_difference = days_difference * 24 * 60
    return minutes_difference

def number_to_words(num):
    p = inflect.engine()
    words = p.number_to_words(num)
    words = words.replace(" and ", " ")
    return words.capitalize()

def main():
    dob_input = input("Enter your date of birth (YYYY-MM-DD): ")

    try:
        year, month, day = dob_input.split('-')
        year = int(year)
        month = int(month)
        day = int(day)
        dob = date(year, month, day)

    except ValueError:
        sys.exit("Please input a date in YYYY-MM-DD format.")

    minutes = minutes_since_birth(dob)
    print(f"{number_to_words(minutes)} minutes")

if __name__ == "__main__":
    main()

# p = inflect.engine()
# This line creates an instance of the engine() class from the inflect library and
# assigns it to the variable p. The inflect library is used to generate singular,
# plural, and readable numbers. It provides an engine that contains methods to
# convert numbers, singular words to plural words, etc.

# return p.number_to_words(num)
# This line calls the number_to_words method of the inflect engine (stored in the variable p)
# with the argument num. This method converts the numerical value into its English
# word representation. For instance, if num was 42, this method would return "forty-two".