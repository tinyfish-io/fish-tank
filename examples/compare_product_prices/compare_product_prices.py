"""This example demonstrates how to compare product prices across websites with query_data() method."""

from agentql.ext.playwright.sync_api import Page
from playwright.sync_api import sync_playwright

# Set the URL to the desired website
BESTBUY_URL = "https://www.bestbuy.com/site/nintendo-switch-oled-model-w-joy-con-white/6470923.p?skuId=6470923"
TARGET_URL = "https://www.target.com/p/nintendo-switch-oled-model-with-white-joy-con/-/A-83887639#lnk=sametab"
NINETENDO_URL = "https://www.nintendo.com/us/store/products/nintendo-switch-oled-model-white-set/"

# Define the queries to get the product price
PRODUCT_INFO_QUERY = """
{
    nintendo_switch
    {
        price
    }
}"""


def print_header():
    """Prints the header for the data table"""
    print(f"{'Website':<25} | {'Product ':<20} | {'Price ':<20} ")
    print("-" * 75)


def print_row(website, product, price):
    """Prints the data row"""
    print(f"{website:<25} | {product:<20} | {price:<20} ")


def main():
    print_header()

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)

        # Create a new AgentQL page instance in the browser for web interactions
        page: Page = browser.new_page()

        page.goto(BESTBUY_URL)

        # Use query_data() method to fetch the price from the BestBuy page
        response = page.query_data(PRODUCT_INFO_QUERY)

        print_row("BestBuy", "Nintendo Switch", response["nintendo_switch"]["price"])

        page.goto(NINETENDO_URL)

        # Use query_data() method to fetch the price from the Nintendo page

        response = page.query_data(PRODUCT_INFO_QUERY)

        print_row("Nintendo site", "Nintendo Switch", response["nintendo_switch"]["price"])

        page.goto(TARGET_URL)

        # Use query_data() method to fetch the price from the Target page

        response = page.query_data(PRODUCT_INFO_QUERY)

        print_row("Target", "Nintendo Switch", response["nintendo_switch"]["price"])

        browser.close()


if __name__ == "__main__":
    main()
