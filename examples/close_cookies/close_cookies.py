"""This example demonstrates how to close popup windows (like promotion form) with AgentQL."""

import time

from agentql.ext.playwright.sync_api import Page
from playwright.sync_api import sync_playwright

# Set the URL to the desired website
URL = "https://www.amazon.com/"

QUERY = """
{
    cookies_form {
        reject_btn
    }
}
"""


def main():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)

        # Create a new AgentQL page instance in the browser for web interactions
        page: Page = browser.new_page()

        page.goto(URL)

        # Use query_elements() method to fetch the cookies dialog button from the page
        response = page.query_elements(QUERY)

        # Check if there is a cookie-rejection button on the page
        if response.cookies_form.reject_btn is not None:

            # If so, click the close button to reject cookies
            response.cookies_form.reject_btn.click()

        # Wait for 5 seconds to see the browser in action
        time.sleep(5)

        browser.close()


if __name__ == "__main__":
    main()
