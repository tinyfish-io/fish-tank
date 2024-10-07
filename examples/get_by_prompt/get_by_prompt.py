"""This example demonstrates how to leverage get_by_prompt method to interact with element by prompt text."""

import agentql
from playwright.sync_api import sync_playwright

# Set the URL to the desired website
URL = "https://thinking-tester-contact-list.herokuapp.com/"


def main():
    with sync_playwright() as p, p.chromium.launch(headless=False) as browser:

        page = agentql.wrap(browser.new_page())  # Wrapped to access AgentQL's query API's

        # Navigate to the URL
        page.goto(URL)

        # Get the sign up button by the prompt text
        sign_up_btn = page.get_by_prompt(prompt="Sign up button")

        # Click the sign up button if it exists
        if sign_up_btn:
            sign_up_btn.click()

        # Used only for demo purposes. It allows you to see the effect of the script.
        page.wait_for_timeout(10000)


if __name__ == "__main__":
    main()
