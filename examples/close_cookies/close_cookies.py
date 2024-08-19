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
    with sync_playwright() as playwright, playwright.chromium.launch(headless=False) as browser:
        # Create a new page in the browser and cast it to custom Page type to get access to the AgentQL's querying API
        page: Page = browser.new_page()  # type: ignore

        page.goto(URL)

        # Use query_elements() method to fetch the cookies dialog button from the page
        response = page.query_elements(QUERY)

        # Check if there is a cookie-rejection button on the page
        if response.cookies_form.reject_btn is not None:

            # If so, click the close button to reject cookies
            response.cookies_form.reject_btn.click()

        # Wait for 10 seconds to see the browser in action
        time.sleep(10)


if __name__ == "__main__":
    main()
