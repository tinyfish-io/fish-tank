"""This example demonstrates how to use AgentQL's Debug Manager to debug the script in asynchronous environment."""

import asyncio
import logging

import agentql
from agentql.async_api import DebugManager
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
    async with DebugManager.debug_mode(), async_playwright() as playwright, await playwright.chromium.launch(
        headless=False
    ) as browser:
        # Create a new page in the browser and wrap it to get access to the AgentQL's querying API
        page = await agentql.wrap_async(browser.new_page())

        await page.goto(URL)

        response = await page.query_elements(QUERY)

        # Buggy code that will crash the script. When it crashes, the debug manager will save debug files to designated directory (~/.agentql/debug by default).
        await response.search.fill("ivysaur")  # type: ignore
        await page.keyboard.press("Enter")


if __name__ == "__main__":
    asyncio.run(main())
