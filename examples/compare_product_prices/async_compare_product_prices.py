"""This example demonstrates how to asynchronously fetch product prices across websites in parallel with query_data() method."""

import asyncio

from agentql.ext.playwright.async_api import Page
from playwright.async_api import BrowserContext, async_playwright

# Set the URL to the desired website
BESTBUY_URL = "https://www.bestbuy.com/site/nintendo-switch-oled-model-w-joy-con-white/6470923.p?skuId=6470923"
TARGET_URL = "https://www.target.com/p/nintendo-switch-oled-model-with-white-joy-con/-/A-83887639#lnk=sametab"
NINETENDO_URL = "https://www.nintendo.com/us/store/products/nintendo-switch-oled-model-white-set/"

# Define the queries to interact with the page
PRODUCT_INFO_QUERY = """
{
    nintendo_switch_price
}
"""


async def fetch_price(context: BrowserContext, session_url, query):
    """Open the given URL in a new tab and fetch the price of the product."""
    # Create a page in a new tab in the broswer context and cast it to custom Page type to get access to the AgentQL's querying API
    page: Page = await context.new_page()  # type: ignore

    await page.goto(session_url)

    # Fetch the price data from the page
    data = await page.query_data(query)
    return data["nintendo_switch_price"]


async def get_price_across_websites():
    """Fetch prices concurrently in the same browser session from multiple websites."""
    async with async_playwright() as playwright, await playwright.chromium.launch(
        headless=False
    ) as browser, await browser.new_context() as context:
        # Open multiple tabs in the same browser context to fetch prices concurrently
        bestbuy_price, nintendo_price, target_price = await asyncio.gather(
            fetch_price(context, BESTBUY_URL, PRODUCT_INFO_QUERY),
            fetch_price(context, NINETENDO_URL, PRODUCT_INFO_QUERY),
            fetch_price(context, TARGET_URL, PRODUCT_INFO_QUERY),
        )

        print(
            f"""
        Price at BestBuy: ${bestbuy_price}
        Price at Ninetendo: ${nintendo_price}
        Price at Target: ${target_price}
        """
        )


if __name__ == "__main__":
    asyncio.run(get_price_across_websites())
