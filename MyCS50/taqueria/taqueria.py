def main():
    prices()

def prices():
    cost = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    total_cost = 0
    while True:
        try:
            item = input("Enter an item name (or 'quit' to stop): ").title()

        except EOFError:
            print(f"Total: ${total_cost:.2f}")
            break
        else:
            if item not in cost:
                # print("This item is not in our database.")
                pass # ignores invalid item and reruns prompt
            else:
                price = get_price(item, cost)
                total_cost += price
                # print(f"${price:.2f}")
                print(f"Total: ${total_cost:.2f}") # Total so far

def get_price(item, cost_dict):
    return cost_dict.get(item, None)

main()
