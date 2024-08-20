"""This example demonstrates how to compare product prices across websites with query_data() method."""

import agentql
from playwright.sync_api import sync_playwright

# Set the URL to the desired website
BESTBUY_URL = "https://www.bestbuy.com/site/nintendo-switch-oled-model-w-joy-con-white/6470923.p?skuId=6470923"
TARGET_URL = "https://www.target.com/p/nintendo-switch-oled-model-with-white-joy-con/-/A-83887639#lnk=sametab"
NINTENDO_URL = "https://www.nintendo.com/us/store/products/nintendo-switch-oled-model-white-set/"

# Define the queries to get the product price
PRODUCT_INFO_QUERY = """
{
    nintendo_switch_price
}
"""


def main():
    with sync_playwright() as playwright, playwright.chromium.launch(headless=False) as browser:
        # Create a new page in the browser and wrap it to get access to the AgentQL's querying API
        page = agentql.wrap(browser.new_page())

        page.goto(BESTBUY_URL)

        # Use query_data() method to fetch the price from the BestBuy page
        response = page.query_data(PRODUCT_INFO_QUERY)

        print("Price at BestBuy: ", response["nintendo_switch_price"])

        page.goto(NINTENDO_URL)

        # Use query_data() method to fetch the price from the Nintendo page
        response = page.query_data(PRODUCT_INFO_QUERY)

        print("Price at Nintendo: ", response["nintendo_switch_price"])

        page.goto(TARGET_URL)

        # Use query_data() method to fetch the price from the Target page
        response = page.query_data(PRODUCT_INFO_QUERY)

        print("Price at Target: ", response["nintendo_switch_price"])


if __name__ == "__main__":
    main()
