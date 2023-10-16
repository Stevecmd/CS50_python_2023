import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    # Capturing both provided time formats
    pattern = r'(\d{1,2}(:\d{2})?) (AM|PM) to (\d{1,2}(:\d{2})?) (AM|PM)'
    match = re.match(pattern, s)
    # If no match then raise an error
    if not match:
        raise ValueError("Invalid format.")

    start_time = convert_to_24_hour(match.group(1), match.group(3))
    end_time = convert_to_24_hour(match.group(4), match.group(6))

    return f"{start_time} to {end_time}"

# function to convert to 24 hrs
def convert_to_24_hour(time, meridiem):
    if ":" in time:
        hour, minute = map(int, time.split(":"))
    else:
        hour, minute = int(time), 0

    # Validating the time
    if hour < 1 or hour > 12 or minute > 59:
        raise ValueError("Invalid time.")

    if meridiem == "PM" and hour != 12:
        hour += 12
    elif meridiem == "AM" and hour == 12:
        hour = 0

    return f"{hour:02}:{minute:02}"

if __name__ == "__main__":
    main()