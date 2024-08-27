"""This script serves as a skeleton template for synchronous AgentQL scripts."""

import logging

import agentql
from agentql.ext.playwright.sync_api import Page
from playwright.sync_api import sync_playwright

# Set up logging
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

# Set the URL to the desired website
URL = "<Replace with the correct url>"


def main():
    with sync_playwright() as p, p.chromium.launch(headless=False) as browser:
        # Create a new page in the browser and wrap it to get access to the AgentQL's querying API
        page = agentql.wrap(browser.new_page())

        # Navigate to the desired URL
        page.goto(URL)

        fetch_data(page)


def fetch_data(page: Page):
    """Fetch data from the page."""
    # Update the query to locate the desired element on the page
    elements_query = """
    {
        search_input
        search_btn
    }
    """

    # Locate desired web elements using AgentQL's query_elements() method
    response = page.query_elements(elements_query)

    # Update to use the actual query terms
    response.search_input.type("<Replace with needed search query>")
    response.search_btn.click()

    # Update the query to fetch the desired data from the page
    data_query = """
    {
        products[] {
            price
        }
    }
    """

    # Fetch the data from the page using AgentQL's query_data() method
    data = page.query_data(data_query)
    # Update to use the actual keys corresponding to query terms
    for result in data["products"]:
        log.info(result["price"])


if __name__ == "__main__":
    main()
