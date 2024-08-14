#!/usr/bin/env python3

"""This is an example of collecting pricing data from e-commerce website using AgentQL."""

# Import the Page class from the AgentQL Playwright extension
# This enables the use of the AgentQL Smart Locator and Data Query API
from agentql.ext.playwright.sync_api import Page

# Import the synchronous playwright library
# This library is used to launch the browser and interact with the web page
from playwright.sync_api import sync_playwright

URL = "https://scrapeme.live/shop"

# The AgentQL query to locate the search box element
# More about AgentQL Query: https://docs.agentql.ai/agentql-query/query-intro
SEARCH_BOX_QUERY = """
{
    search_product_box
}
"""

# The AgentQL query of the data to be extracted
# More about AgentQL Query: https://docs.agentql.ai/agentql-query/query-intro
PRODUCT_DATA_QUERY = """
{
    price_currency
    products[] {
        name
        price
    }
}
"""


def main():
    with sync_playwright() as playwright:
        # Launch the Playwright browser
        browser = playwright.chromium.launch(headless=False)

        # Create a new page in the broswer and cast it to custom Page type to get access to the AgentQL's querying API
        page: Page = browser.new_page()  # type: ignore

        page.goto(URL)

        product_data = _extract_product_data(
            page,
            search_key_word="fish",
        )

        # Close the browser to free up resources
        browser.close()

        print(product_data)


def _extract_product_data(page: Page, search_key_word: str) -> dict:
    """Extract product data.

    Args:
        page (Page): The Playwright page object to interact with the browser.
        search_key_word (str): The product to search for.

    Returns:
        dict: The product data extracted from the page.
    """
    # Find DOM element using AgentQL Elements Query API
    response = page.query_elements(SEARCH_BOX_QUERY)

    # Interact with the element using Playwright API
    # API Doc: https://playwright.dev/python/docs/input#text-input
    response.search_product_box.type(search_key_word, delay=200)
    page.keyboard.press("Enter")

    # Extract data using AgentQL Data Query API
    data = page.query_data(PRODUCT_DATA_QUERY)

    return data


if __name__ == "__main__":
    main()
