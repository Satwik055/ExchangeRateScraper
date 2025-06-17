import requests
from bs4 import BeautifulSoup
from currency import *
from utils import *
from loguru import logger


def scrape_exchange_rate(currency: Currency) -> float:
    try:
        # Send HTTP GET request
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(currency.value, headers=headers)
        response.raise_for_status()

        # Parse HTML with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find element with data-last-price attribute
        element = soup.find(attrs={"data-last-price": True})

        if element:
            last_price = element['data-last-price']
            logger.info(f"Fetched exchanged rate of {currency}: {last_price}")
            return round(float(last_price), 2)
        else:
            raise Exception("No element with data-last-price attribute found")

    except Exception as e:
        raise Exception(f"Error occurred: {e}")


# Example usage
if __name__ == "__main__":
    price = scrape_exchange_rate(Currency.CAD)

    if price is not None:
        print(f"Last price: {add_commission(price)}")
    else:
        print("Failed to scrape the price")
