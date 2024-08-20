"""This example demonstrates how to asynchronously fetch product prices across websites in parallel with query_data() method."""

import asyncio

import agentql
from playwright.async_api import BrowserContext, async_playwright

# Set the URL to the desired website
BESTBUY_URL = "https://www.bestbuy.com"
TELQUEST_URL = "https://www.telquestintl.com"
EBAY_URL = "https://www.ebay.com"

# Define the queries to interact with the page
HOME_PAGE_QUERY = """
{
    search_input
    search_button
}
"""

PRODUCT_PAGE_QUERY = """
{
    nintendo_switch_oled_model_white
}
"""

PRODUCT_INFO_QUERY = """
{
    nintendo_switch_price
}
"""


async def fetch_price(context: BrowserContext, session_url, query):
    """Open the given URL in a new tab and fetch the price of the product."""
    # Create a page in a new tab in the broswer context and wrap it to get access to the AgentQL's querying API
    page = await agentql.wrap_async(context.new_page())
    await page.goto(session_url)

    # Search for the product
    home_response = await page.query_elements(HOME_PAGE_QUERY)
    await home_response.search_input.fill("Nintendo Switch - OLED Model White")
    await home_response.search_button.click()

    # Click on product link
    product_page_response = await page.query_elements(PRODUCT_PAGE_QUERY)
    await product_page_response.nintendo_switch_oled_model_white.click()

    # Fetch the price data from the page
    data = await page.query_data(query)
    return data["nintendo_switch_price"]


async def get_price_across_websites():
    """Fetch prices concurrently in the same browser session from multiple websites."""
    async with async_playwright() as playwright, await playwright.chromium.launch(
        headless=False
    ) as browser, await browser.new_context() as context:
        # Open multiple tabs in the same browser context to fetch prices concurrently
        bestbuy_price, ebay_price, telquest_price = await asyncio.gather(
            fetch_price(context, BESTBUY_URL, PRODUCT_INFO_QUERY),
            fetch_price(context, EBAY_URL, PRODUCT_INFO_QUERY),
            fetch_price(context, TELQUEST_URL, PRODUCT_INFO_QUERY),
        )

        print(
            f"""
        Price at BestBuy: ${bestbuy_price}
        Price at Ebay: ${ebay_price}
        Price at Telquest: ${telquest_price}
        """
        )


if __name__ == "__main__":
    asyncio.run(get_price_across_websites())
