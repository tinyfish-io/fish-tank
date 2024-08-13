"""This example demonstrates how to use AgentQL's Debug Manager to debug the script in asynchronous environment."""

import asyncio
import logging

from agentql.async_api import DebugManager
from agentql.ext.playwright.async_api import Page
from playwright.async_api import async_playwright

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

URL = "https://scrapeme.live/shop/"

# Define the queries to interact with the page
QUERY = """
{
    search_products_box
}
"""


async def main():
    # The following async context manager will enable debug mode for the script.
    async with DebugManager.debug_mode(), async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)

        # Create a new page in the broswer and cast it to custom Page type to get access to the AgentQL's querying API
        page: Page = await browser.new_page()  # type: ignore

        await page.goto(URL)

        response = await page.query_elements(QUERY)

        # Buggy code that will crash the script. When it crashes, the debug manager will save debug files to designated directory (~/.agentql/debug by default).
        await response.search.fill("ivysaur") # type: ignore
        await page.keyboard.press("Enter")

        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
