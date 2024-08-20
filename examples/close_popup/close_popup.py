"""This example demonstrates how to close popup windows (like promotion form) with AgentQL."""

import time

import agentql
from playwright.sync_api import sync_playwright

# Set the URL to the desired website
URL = "https://kinfield.com/"

QUERY = """
{
    popup_form {
        close_btn
    }
}
"""


def main():
    with sync_playwright() as playwright, playwright.chromium.launch(headless=False) as browser:
        # Create a new page in the browser and wrap it to get access to the AgentQL's querying API
        page = agentql.wrap(browser.new_page())

        page.goto(URL)

        # Use query_elements() method to fetch the close popup button from the page
        response = page.query_elements(QUERY)

        # Click the close button to close the popup
        response.popup_form.close_btn.click()

        # Wait for 5 seconds to see the browser in action
        time.sleep(5)


if __name__ == "__main__":
    main()
