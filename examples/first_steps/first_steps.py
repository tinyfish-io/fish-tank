#!/usr/bin/env python3

"""This is an example of collecting pricing data from e-commerce website using AgentQL."""

# Import the Page class from the AgentQL Playwright extension
# This enables the use of the AgentQL Smart Locator and Data Query API
import agentql
from agentql.ext.playwright.sync_api import Page

# Import the synchronous playwright library
# This library is used to launch the browser and interact with the web page
from playwright.sync_api import sync_playwright

URL = "https://scrapeme.live/shop"

# The AgentQL query to locate the search box element
# More about AgentQL Query: https://docs.agentql.com/agentql-query/query-intro
SEARCH_BOX_QUERY = """
{
    search_product_box
}
"""

# The AgentQL query of the data to be extracted
# More about AgentQL Query: https://docs.agentql.com/agentql-query/query-intro
PRODUCT_DATA_QUERY = """
{
    price_currency
    products[] {
        name
        price
    }
}
"""

# Other than the AgentQL query, you can also use natural language prompt to locate the element
NATURAL_LANGUAGE_PROMPT = "Button to display Qwilfish page"


def main():
    with sync_playwright() as playwright, playwright.chromium.launch(headless=False) as browser:
        # Create a new page in the browser and wrap it get access to the AgentQL's querying API
        page = agentql.wrap(browser.new_page())

        page.goto(URL)

        product_data = _extract_product_data(
            page,
            search_key_word="fish",
        )

        print(product_data)

        _add_qwilfish_to_cart(page)


def _extract_product_data(page: Page, search_key_word: str) -> dict:
    """Extract product data.

    Args:
        page (Page): The Playwright page object to interact with the browser.
        search_key_word (str): The product to search for.

    Returns:
        dict: The product data extracted from the page.
    """
    # Find DOM element using AgentQL API's query_elements() method
    response = page.query_elements(SEARCH_BOX_QUERY)

    # Interact with the element using Playwright API
    # API Doc: https://playwright.dev/python/docs/input#text-input
    response.search_product_box.type(search_key_word, delay=200)
    page.keyboard.press("Enter")

    # Extract data using AgentQL API's query_data() method
    data = page.query_data(PRODUCT_DATA_QUERY)

    return data


def _add_qwilfish_to_cart(page: Page):
    """Add Qwilfish to cart with AgentQL Smart Locator API.

    Args:
        page (Page): The Playwright page object to interact with the browser.
    """
    # Find DOM element using AgentQL API's get_by_prompt() method
    qwilfish_page_btn = page.get_by_prompt(NATURAL_LANGUAGE_PROMPT)

    # Interact with the element using Playwright API
    # API Doc: https://playwright.dev/python/docs/api/class-locator#locator-click
    if qwilfish_page_btn:
        qwilfish_page_btn.click()

    # Wait for 10 seconds to see the browser action
    page.wait_for_timeout(10000)


if __name__ == "__main__":
    main()
