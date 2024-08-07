#!/usr/bin/env python3

"""This is an example of collecting pricing data from e-commerce website using AgentQL."""

from playwright.sync_api import sync_playwright

# Import the Page class from the AgentQL Playwright extension
# This enables the use of the AgentQL Smart Locator and Data Query API
from agentql.ext.playwright.sync_api import Page

URL = "https://scrapeme.live/shop"


def main():
    with sync_playwright() as playwright:
        with playwright.chromium.launch(headless=False) as browser:
            page: Page = browser.new_page()
            page.goto(URL)

            product_data = _extract_product_data(
                page,
                search_key_word="fish",
            )

            print(product_data)


def _extract_product_data(page: Page, search_key_word: str) -> dict:
    """Extract product data.

    Args:
        page (Page): The Playwright page object to interact with the browser.
        search_key_word (str): The product to search for.

    Returns:
        dict: The product data extracted from the page.
    """
    # Find DOM element using AgentQL Smart Locator with natural language description
    search_input = page.get_by_prompt("the searchbox for products")

    # Interact with the element using Playwright API
    # API Doc: https://playwright.dev/python/docs/input#text-input
    search_input.type(search_key_word, delay=200)
    search_input.press("Enter")

    # The AgentQL query of the data to be extracted
    # More about AgentQL Query: TODO (Update link)
    # https://agentql-docs.vercel.app/agentql-query/query-intro
    query = """
    {
        price_currency
        products[] {
            name
            price
        }
    }
    """

    # Extract data using AgentQL Data Query API
    data = page.query_data(query)

    return data


if __name__ == "__main__":
    main()
