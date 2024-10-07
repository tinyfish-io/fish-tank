"""This example demonstrates how to login into websites by retrieving and interacting with web elements in AgentQL."""

import agentql
from playwright.sync_api import sync_playwright

# Set the URL to the desired website
URL = "https://practicetestautomation.com/practice-test-login/"

LOGIN_QUERY = """
{
    username_field
    password_field
    submit_btn
}
"""


def main():
    with sync_playwright() as p, p.chromium.launch(headless=False) as browser:

        page = agentql.wrap(browser.new_page())  # Wrapped to access AgentQL's query API

        # Navigate to the URL
        page.goto(URL)

        # Get the username and password fields
        response = page.query_elements(LOGIN_QUERY)

        # Fill the username and password fields
        response.username_field.fill("student")
        response.password_field.fill("Password123")

        # Click the submit button
        response.submit_btn.click()

        # Used only for demo purposes. It allows you to see the effect of the script.
        page.wait_for_timeout(10000)


if __name__ == "__main__":
    main()
