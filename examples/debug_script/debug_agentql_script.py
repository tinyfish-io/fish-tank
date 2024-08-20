"""This example demonstrates how to use AgentQL's Debug Manager to debug the script in synchronous environment."""

import logging

import agentql
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
    with DebugManager.debug_mode(), sync_playwright() as playwright, playwright.chromium.launch(
        headless=False
    ) as browser:
        # Create a new page in the browser and wrap it to get access to the AgentQL's querying API
        page = agentql.wrap(browser.new_page())

        page.goto(URL)

        response = page.query_elements(QUERY)

        # Buggy code that will crash the script. When it crashes, the debug manager will save debug files to designated directory (~/.agentql/debug by default).
        response.search.fill("ivysaur")  # type: ignore
        page.keyboard.press("Enter")


if __name__ == "__main__":
    main()
