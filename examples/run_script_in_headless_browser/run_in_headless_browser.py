"""This example demonstrates how to run the script in headless browser."""

from agentql.ext.playwright.sync_api import Page
from playwright.sync_api import sync_playwright

# Set the URL to the desired website
URL = "https://google.com"

QUERY = """
{
    search_input
    search_btn
}
"""

QUERY_2 = """
{
    president_name
}
"""


def main():
    with sync_playwright() as playwright:
        # Launch the browser in headless mode
        browser = playwright.chromium.launch(headless=True)

        # Create a new AgentQL page instance in the browser for web interactions
        page: Page = browser.new_page()

        page.goto(URL)

        # Use query_elements() method to fetch the search box and button from the page

        response = page.query_elements(QUERY)

        response.search_input.fill("President of United States")

        response.search_btn.click(force=True)

        # Use query_data() method to fetch the URLs from the page
        response = page.query_data(QUERY_2)

        print(response)

        browser.close()


if __name__ == "__main__":
    main()
