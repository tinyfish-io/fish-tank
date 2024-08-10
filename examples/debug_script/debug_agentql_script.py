"""This example demonstrates how to use AgentQL's Debug Manager to debug the script in synchronous environment."""

import logging

from agentql.ext.playwright.sync_api import Page
from agentql.sync_api import DebugManager
from playwright.sync_api import sync_playwright

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

URL = "https://google.com"

# Define the queries to interact with the page
QUERY = """
    {
        search_box
        search_btn
        about_link
    }
    """


def main():
    # The first context manager below will enable debug mode for the script.
    with DebugManager.debug_mode(), sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)

        # Create a new AgentQL page instance in the browser for web interactions
        page: Page = browser.new_page()

        page.goto(URL)

        response = page.query_elements(QUERY)

        # Buggy code that will crash the script. When it crashes, the debug manager will save debug files to designated directory (~/.agentql/debug by default).
        response.search.fill("tinyfish")
        response.search_btn.click(force=True)

        browser.close()


if __name__ == "__main__":
    main()
