# start by installing validators
# pip install validators

import validators

def main():
    # Get the email input
    email_address = input("Please enter an email address: ")

    # Checking if the email address is valid using the validators library
    # that was installed previously
    if validators.email(email_address):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()
