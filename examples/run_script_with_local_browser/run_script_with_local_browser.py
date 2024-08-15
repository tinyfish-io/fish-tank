"""This example demonstrates how to run the script in an existing local browser with AgentQL."""

from agentql.ext.playwright.sync_api import Page
from playwright.sync_api import sync_playwright

# The URL to connect to your local existing browser.
WEBSOCKET_URL = "YOUR_WEBSOCKET_URL"

URL = "https://scrapeme.live/shop"

QUERY = """
{
    tours[] {
        title
        price
        length
    }
}
"""

QUERY_FOR_SCRAPE_ME_1 = """
{
    search_products_box
}
"""

QUERY_FOR_SCRAPE_ME_2 = """
{
    number_in_stock
}
"""


def fetch_data_from_open_website_page():
    """This function demonstrates how to fetch data from open pages in your local browser."""
    with sync_playwright() as p:
        # Connect to the existing browser via Chrome DevTools Protocol
        browser = p.chromium.connect_over_cdp(WEBSOCKET_URL)

        # Get the first page from the opened browser
        page: Page = browser.contexts[0].pages[0]  # type: ignore

        # Use query_elements() method to locate the search box and search button from the page
        response = page.query_data(QUERY)

        print(response)


def interact_with_new_page_in_local_browser():
    """This function demonstrates how to open and interact with a new page your local browser."""
    with sync_playwright() as p:
        # Connect to the existing browser via Chrome DevTools Protocol
        browser = p.chromium.connect_over_cdp(WEBSOCKET_URL)

        # Create a new tab in the existing browser window
        page: Page = browser.contexts[0].new_page()  # type: ignore

        page.goto(URL)

        # Use query_elements() method to locate the search product box from the page
        response = page.query_elements(QUERY_FOR_SCRAPE_ME_1)

        # Use Playwright's API to fill the search box and press Enter
        response.search_products_box.type("Charmander")
        page.keyboard.press("Enter")

        # Use query_data() method to fetch the stock number from the page
        response = page.query_data(QUERY_FOR_SCRAPE_ME_2)

        print(response)

        # Close the browser here will close your local browser
        browser.close()


if __name__ == "__main__":
    interact_with_new_page_in_local_browser()
