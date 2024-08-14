"""This example demonstrates how to get XPath of an element that was fetched with AgentQL."""

from agentql.ext.playwright.sync_api import Page
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
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)

        # Create a new page in the broswer and cast it to custom Page type to get access to the AgentQL's querying API
        page: Page = browser.new_page()  # type: ignore

        page.goto(URL)

        # Use query_elements() method to fetch the search box from the page
        response = page.query_elements(QUERY)

        # Get the XPath
        print("XPath:", xpath_path(response.search_products_box))

        browser.close()


if __name__ == "__main__":
    main()
