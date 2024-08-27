"""This script serves as a skeleton template for asynchronous AgentQL scripts."""

import asyncio
import logging

import agentql
from playwright.async_api import BrowserContext, async_playwright

# Set up logging
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

# Set URLs to the desired websites
WEBSITE_URL_1 = "<Replace with the correct url>"
WEBSITE_URL_2 = "<Replace with the correct url>"
WEBSITE_URL_3 = "<Replace with the correct url>"


async def main():
    """Fetch data concurrently in the same browser session from multiple websites."""
    async with async_playwright() as p, await p.chromium.launch(
        headless=False
    ) as browser, await browser.new_context() as context:
        # Open multiple tabs in the same browser context to fetch data concurrently
        await asyncio.gather(
            fetch_data(context, WEBSITE_URL_1),
            fetch_data(context, WEBSITE_URL_2),
            fetch_data(context, WEBSITE_URL_3),
        )


async def fetch_data(context: BrowserContext, session_url):
    """Open the given URL in a new tab and fetch the data."""
    # Create a page in a new tab in the broswer context and wrap it to get access to the AgentQL's querying API
    page = await agentql.wrap_async(context.new_page())
    await page.goto(session_url)

    # Update the query to locate the desired element on the page
    elements_query = """
    {
        search_input
        search_btn
    }
    """

    # Locate desired web elements using AgentQL's query_elements() method
    response = await page.query_elements(elements_query)
    # Update to use the actual query terms to interact with the elements
    await response.search_input.type("<Replace with needed search query>")
    await response.search_button.click()

    # Update the query to fetch the desired data from the page
    data_query = """
    {
        products[] {
            name
            price
        }
    }
    """

    # Fetch the data from the page using AgentQL's query_data() method
    data = await page.query_data(data_query)
    # Update to use the actual keys corresponding to query terms
    log.info(f"Prices fetched from {session_url}:")
    for product in data["products"]:
        log.info(f"Product: {product['name']}, Price: {product['price']}")


if __name__ == "__main__":
    # Run the main function in an event loop
    asyncio.run(main())
