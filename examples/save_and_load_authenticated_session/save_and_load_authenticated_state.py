"""This example demonstrates how to save and load a authenticated state (i.e. signed-in state) using AgentQL."""

import agentql
from playwright.sync_api import sync_playwright

URL = "https://www.yelp.com/"
EMAIL = "REPLACE_WITH_YOUR_EMAIL (For yelp.com)"
PASSWORD = "REPLACE_WITH_YOUR_PASSWORD (For yelp.com)"

# Define the queries to interact with the page
LOG_IN_QUERY = """
{
    log_in_btn
}
"""

CREDENTIALS_QUERY = """
{
    sign_in_form {
        email_input
        password_input
        log_in_btn
    }
}
"""


def save_signed_in_state():
    with sync_playwright() as playwright, playwright.chromium.launch(headless=False) as browser:
        # Create a new page in the browser and wrap it to get access to the AgentQL's querying API
        page = agentql.wrap(browser.new_page())

        page.goto(URL)

        # Use query_elements() method to locate "Log In" button on the page
        response = page.query_elements(LOG_IN_QUERY)
        # Use Playwright's API to click located button
        response.log_in_btn.click()

        # Use query_elements() method to locate email, password input fields, and "Log In" button in sign-in form
        response_credentials = page.query_elements(CREDENTIALS_QUERY)
        # Fill the email and password input fields
        response_credentials.sign_in_form.email_input.fill(EMAIL)
        response_credentials.sign_in_form.password_input.fill(PASSWORD)
        response_credentials.sign_in_form.log_in_btn.click()

        page.wait_for_page_ready_state()

        # wait for timeout in order to save state
        page.wait_for_timeout(5000)

        # Save the signed-in state
        browser.contexts[0].storage_state(path="yelp_login.json")


def load_signed_in_state():
    with sync_playwright() as playwright, playwright.chromium.launch(headless=False) as browser:
        # Load the saved signed-in session by creating a new browser context with the saved signed-in state
        context = browser.new_context(storage_state="yelp_login.json")

        # Create a new page in the browser and wrap it to get access to the AgentQL's querying API
        page = agentql.wrap(context.new_page())

        page.goto(URL)

        page.wait_for_page_ready_state()

        # Wait for 10 seconds to see the signed-in page
        page.wait_for_timeout(10000)


if __name__ == "__main__":
    save_signed_in_state()
    load_signed_in_state()
