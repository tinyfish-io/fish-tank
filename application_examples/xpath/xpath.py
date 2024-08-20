"""This example demonstrates how to get XPath of an element that was fetched with AgentQL."""

import agentql
from playwright.sync_api import sync_playwright

# import https://pypi.org/project/playwright-dompath/
# Playwright Dompath is a Python library that helps you to generate XPath from Playwright selectors.
from playwright_dompath.dompath_sync import xpath_path

URL = "https://scrapeme.live/shop/"

QUERY = """
{
    search_products_box
}
"""


def main():
    with sync_playwright() as playwright, playwright.chromium.launch(headless=False) as browser:
        # Create a new page in the browser and wrap it to get access to the AgentQL's querying API
        page = agentql.wrap(browser.new_page())

        page.goto(URL)

        # Use query_elements() method to fetch the search box from the page
        response = page.query_elements(QUERY)

        # Get the XPath
        print("XPath:", xpath_path(response.search_products_box))


if __name__ == "__main__":
    main()
