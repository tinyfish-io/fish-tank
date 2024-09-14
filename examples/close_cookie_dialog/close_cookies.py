"""This example demonstrates how to close popup windows (like promotion form) with AgentQL."""

import agentql
from playwright.sync_api import sync_playwright

# Set the URL to the desired website
URL = "https://gov.uk/"

QUERY = """
{
    cookies_form {
        reject_btn
    }
}
"""


def main():
    with sync_playwright() as playwright, playwright.chromium.launch(headless=False) as browser:
        # Create a new page in the browser and wrap it to get access to the AgentQL's querying API
        page = agentql.wrap(browser.new_page())

        page.goto(URL)

        # Use query_elements() method to fetch the cookies dialog button from the page
        response = page.query_elements(QUERY)

        # Check if there is a cookie-rejection button on the page
        if response.cookies_form.reject_btn != None:
            # If so, click the close button to reject cookies
            response.cookies_form.reject_btn.click()

        # Wait for 10 seconds to see the browser in action
        page.wait_for_timeout(10000)


if __name__ == "__main__":
    main()
