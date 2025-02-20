import requests
import sys

EXCHANGE_RATE_URL = "https://api.exchangerate-api.com/v4/latest/USD"

def convert_currency(target_currency, amount):
    """Fetch and convert currency from USD to the specified target currency"""
    response = requests.get(EXCHANGE_RATE_URL)

    if response.status_code == 200:
        rates = response.json()["rates"]
        if target_currency in rates:
            converted_amount = amount * rates[target_currency]
            print(f"{amount} USD is {converted_amount:.2f} {target_currency}")
        else:
            print("Currency not supported.")
    else:
        print("Failed to fetch exchange rates.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python currency_converter.py <currency_code> <amount>")
    else:
        convert_currency(sys.argv[1].upper(), float(sys.argv[2]))
