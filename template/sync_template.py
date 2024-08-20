"""This script serves as a skeleton template for synchronous AgentQL scripts."""

import logging

import agentql
from agentql.ext.playwright.sync_api import Page
from playwright.sync_api import sync_playwright

# Set up logging
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

# Set the URL to the desired website
URL = "WEBSITE_URL"

# Update the query to locate the desired element on the page
ELEMENTS_QUERY = """
{
    search_input
    search_btn
}
"""

# Update the query to fetch the desired data from the page
DATA_QUERY = """
{
    products[] {
        price
    }
}
"""


def main():
    with sync_playwright() as playwright, playwright.chromium.launch(headless=True) as browser:
        # Create a new page in the browser and wrap it to get access to the AgentQL's querying API
        page = agentql.wrap(browser.new_page())

        # Navigate to the desired URL
        page.goto(URL)

        interact_with_elements(page)

        fetch_data(page)


def interact_with_elements(page: Page):
    """Locate and interact with desired web elements."""
    # Locate desired web elements using AgentQL's query_elements() method
    response = page.query_elements(ELEMENTS_QUERY)

    # Update to use the actual query terms
    response.search_btn.click()
    response.search_input.fill("search query")


def fetch_data(page: Page):
    """Fetch data from the page."""
    # Fetch the data from the page using AgentQL's query_data() method
    data = page.query_data(DATA_QUERY)

    # Update to use the actual keys corresponding to query terms
    for result in data["products"]:
        log.info(result["price"])


if __name__ == "__main__":
    main()
