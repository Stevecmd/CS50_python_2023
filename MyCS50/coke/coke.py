# In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time,
# each time informing the user of the amount due. Once the user has inputted at least 50 cents,
# output how many cents in change the user is owed.
# Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.

# ACCEPTED_DENOMINATIONS = [5, 10, 25]
# MINIMUM_AMOUNT = 50

# def main():
#     total = 0
#     while total < MINIMUM_AMOUNT:
#         coin = int(input("Please insert a coin. Acceptable denominations are 25, 10, and 5 cents: "))
#         if coin in ACCEPTED_DENOMINATIONS:
#             total += coin
#             print("You have inserted", total, "cents.")
#             if total < MINIMUM_AMOUNT:
#                 print("Amount due: ", MINIMUM_AMOUNT - total, "cents.")
#             elif total > MINIMUM_AMOUNT:
#                 print("Change owed: ", total - MINIMUM_AMOUNT, "cents.")
#         else:
#             print("That's not a valid coin denomination. Please try again.")
#     print(f"You have inserted at least {total} cents. Thank you for shopping with us!.")

# main()

ACCEPTED_DENOMINATIONS = [5, 10, 25]
MINIMUM_AMOUNT = 50

def main():
    total = 0
    while total < MINIMUM_AMOUNT:
        coin = int(input("Please insert a coin. Acceptable denominations are 25, 10, and 5 cents: "))
        if coin in ACCEPTED_DENOMINATIONS:
            total += coin
            if total < MINIMUM_AMOUNT:
                # print("You have inserted", total, "cents. Amount due: ", MINIMUM_AMOUNT - total, "cents.")
                print("Amount Due:",MINIMUM_AMOUNT - total)
        else:
            # print("That's not a valid coin denomination. Please try again.")
            print("Amount Due:",MINIMUM_AMOUNT - total)
    if total == MINIMUM_AMOUNT:
        # print(f"You have inserted exactly {total} cents. Thank you for shopping with us!")
        print(f"Change Owed: {total - MINIMUM_AMOUNT}")
    elif total > MINIMUM_AMOUNT:
        # print(f"You have inserted {total} cents. Change owed: {total - MINIMUM_AMOUNT} cents.")
        print(f"Change Owed: {total - MINIMUM_AMOUNT}")

main()