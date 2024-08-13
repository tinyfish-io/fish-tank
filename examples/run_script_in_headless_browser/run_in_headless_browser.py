"""This example demonstrates how to run the script in headless browser."""

from agentql.ext.playwright.sync_api import Page
from playwright.sync_api import sync_playwright

# Set the URL to the desired website
URL = "https://scrapeme.live/shop"

QUERY = """
{
    search_products_box
}
"""

QUERY_2 = """
{
    number_in_stock
}
"""


def main():
    with sync_playwright() as playwright:
        # Launch the browser in headless mode
        browser = playwright.chromium.launch(headless=False)

        # Create a new page in the broswer and cast it to custom Page type to get access to the AgentQL's querying API
        page: Page = browser.new_page()  # type: ignore

        page.goto(URL)

        # Use query_elements() method to locate the search box and search button from the page
        response = page.query_elements(QUERY)

        # Use Playwright's API to fill the search box and press Enter
        response.search_products_box.type("Charmander")
        page.keyboard.press("Enter")

        # Use query_data() method to fetch the president name from the page
        response = page.query_data(QUERY_2)

        print(response)

        browser.close()


if __name__ == "__main__":
    main()
