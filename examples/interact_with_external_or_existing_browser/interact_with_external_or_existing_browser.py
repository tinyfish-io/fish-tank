"""This example demonstrates how to interact with an external or existing browser with AgentQL."""

import agentql
from playwright.sync_api import sync_playwright

# The URL of the external or existing browser you wish to connect.
WEBSOCKET_URL = "http://localhost:9222"

URL = "https://scrapeme.live/shop"

VIATOR_TOURS_QUERY = """
{
    tours[] {
        title
        price
        length
    }
}
"""

SEARCH_QUERY = """
{
    search_products_box
}
"""

STOCK_QUERY = """
{
    number_in_stock
}
"""


def fetch_data_from_open_website_page():
    """This function demonstrates how to fetch data from open pages in your local browser."""
    with sync_playwright() as p:
        # Connect to the browser via Chrome DevTools Protocol
        browser = p.chromium.connect_over_cdp(WEBSOCKET_URL)

        # Get the first page from the opened browser and wrap it to get access to the AgentQL's querying API
        page = agentql.wrap(browser.contexts[0].pages[0])

        # Use query_data() method to fetch the data from the page
        response = page.query_data(VIATOR_TOURS_QUERY)

        print(response)


def interact_with_new_page_in_local_browser():
    """This function demonstrates how to open and interact with a new page your local browser."""
    with sync_playwright() as p:
        # Connect to the browser via Chrome DevTools Protocol
        browser = p.chromium.connect_over_cdp(WEBSOCKET_URL)

        # Create a new tab in the browser window and wrap it to get access to the AgentQL's querying API
        page = agentql.wrap(browser.contexts[0].new_page())

        page.goto(URL)

        # Use query_elements() method to locate the search product box from the page
        response = page.query_elements(SEARCH_QUERY)

        # Use Playwright's API to fill the search box and press Enter
        response.search_products_box.type("Charmander")
        page.keyboard.press("Enter")

        # Use query_data() method to fetch the stock number from the page
        response = page.query_data(STOCK_QUERY)

        print(response)


if __name__ == "__main__":
    interact_with_new_page_in_local_browser()
