"""This example demonstrates how to use AgentQL's Debug Manager to debug the script in synchronous environment."""

import logging

from agentql.ext.playwright.sync_api import Page
from agentql.sync_api import DebugManager
from playwright.sync_api import sync_playwright

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

URL = "https://scrapeme.live/shop/"

# Define the queries to interact with the page
QUERY = """
{
    search_products_box
}
"""


def main():
    # The first context manager below will enable debug mode for the script.
    with DebugManager.debug_mode(), sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)

        # Create a new page in the broswer and cast it to custom Page type to get access to the AgentQL's querying API
        page: Page = browser.new_page()  # type: ignore

        page.goto(URL)

        response = page.query_elements(QUERY)

        # Buggy code that will crash the script. When it crashes, the debug manager will save debug files to designated directory (~/.agentql/debug by default).
        response.search.fill("ivysaur")
        page.keyboard.press("Enter")

        browser.close()


if __name__ == "__main__":
    main()
