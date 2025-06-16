from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from enum import Enum
from currency import *
import time
import logging

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
handler.setFormatter(formatter)

logger = logging.getLogger("rate_scraper_module_logger")
logger.setLevel(logging.INFO)
logger.addHandler(handler)


def scrape_exchange_rate(currency: Currency) -> float:
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = None
    try:
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(currency.value)

        # Wait for the exchange rate element to load
        rate_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".YMlKec.fxKbKc"))
        )

        # Extract and clean the rate
        rate_text = rate_element.text.strip()
        try:
            rate = round(float(rate_text.replace(",", "")), 2)
            logger.info(f"Successfully scraped rate for {currency}: {rate} ")
            return rate

        except ValueError as e:
            raise RuntimeError(f"Failed to parse rate value: {rate_text}") from e

    except Exception as e:
        raise RuntimeError(f"Failed to scrape exchange rate: {str(e)}")
    finally:
        if driver:
            driver.quit()
