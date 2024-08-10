"""This example demonstrates how to use AgentQL's Debug Manager to debug the script in asynchronous environment."""

import asyncio
import logging

from agentql.async_api import DebugManager
from agentql.ext.playwright.async_api import Page
from playwright.async_api import async_playwright

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


async def main():
    # The following async context manager will enable debug mode for the script.
    async with DebugManager.debug_mode(), async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)

        # Create a new AgentQL page instance in the browser for web interactions
        page: Page = await browser.new_page()

        await page.goto(URL)

        response = await page.query_elements(QUERY)

        # Buggy code that will crash the script. When it crashes, the debug manager will save debug files to designated directory (~/.agentql/debug by default).
        await response.search.fill("tinyfish")
        await response.search_btn.click(force=True)

        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
