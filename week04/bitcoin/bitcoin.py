# Make sure "pip install requests" has been run atleast once

# Soln
import requests
import sys

def main():
    # Get the desired bitcoin amount from the user's command-line argument
    desired_bitcoin_amount = get_user_input()

    # Fetch the current price of Bitcoin in USD
    current_bitcoin_price_usd = fetch_current_bitcoin_price()

    # Calculate the total cost in USD for the desired Bitcoin amount
    total_cost_usd = desired_bitcoin_amount * current_bitcoin_price_usd

    # Display the total cost to the user
    print(f'${total_cost_usd:,.4f}')

def get_user_input():
    """Retrieve and validate the number of bitcoins from command-line argument."""
    try:
        bitcoin_amount = float(sys.argv[1])
        return bitcoin_amount
    except IndexError:
        sys.exit("Error: Missing command-line argument.")
    except ValueError:
        sys.exit("Error: Command-line argument is not a valid number.")

def fetch_current_bitcoin_price():
    # Fetch the current price of Bitcoin in USD.
    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        bitcoin_data = response.json()
        return float(bitcoin_data['bpi']['USD']['rate_float'])
    except requests.RequestException:
        sys.exit("Error: Unable to fetch Bitcoin price from the API.")
    except (KeyError, ValueError):
        sys.exit("Error: Unexpected data format from the API.")

if __name__ == "__main__":
    main()
