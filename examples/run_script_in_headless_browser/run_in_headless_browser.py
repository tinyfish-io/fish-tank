"""This example demonstrates how to run the script in headless browser."""

import agentql
from playwright.sync_api import sync_playwright

# Set the URL to the desired website
URL = "https://scrapeme.live/shop"

SEARCH_QUERY = """
{
    search_products_box
}
"""

STOCK_NUMBER_QUERY = """
{
    number_in_stock
}
"""


def main():
    with sync_playwright() as playwright, playwright.chromium.launch(headless=True) as browser:
        # Create a new page in the browser and wrap it to get access to the AgentQL's querying API
        page = agentql.wrap(browser.new_page())

        page.goto(URL)

        # Use query_elements() method to locate the search product box from the page
        response = page.query_elements(SEARCH_QUERY)

        # Use Playwright's API to fill the search box and press Enter
        response.search_products_box.type("Charmander")
        page.keyboard.press("Enter")

        # Use query_data() method to fetch the stock number from the page
        response = page.query_data(STOCK_NUMBER_QUERY)

        print(response)


if __name__ == "__main__":
    main()
