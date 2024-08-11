"""This example demonstrates how to asynchronously compare product prices across websites with query_data() method."""

import asyncio

from agentql.ext.playwright.async_api import Page
from playwright.async_api import async_playwright

# Set the URL to the desired website
BESTBUY_URL = "https://www.bestbuy.com/site/nintendo-switch-oled-model-w-joy-con-white/6470923.p?skuId=6470923"
TARGET_URL = "https://www.target.com/p/nintendo-switch-oled-model-with-white-joy-con/-/A-83887639#lnk=sametab"
NINETENDO_URL = "https://www.nintendo.com/us/store/products/nintendo-switch-oled-model-white-set/"

# Define the queries to interact with the page
PRODUCT_INFO_QUERY = """
{
    nintendo_switch
    {
        price
    }
}"""


def print_header():
    """Prints the header for the data table"""
    print(f"{'Website':<25} | {'Product ':<20} | {'Price ':<20} ")
    print("-" * 75)


def print_row(website, product, price):
    """Prints the data row"""
    print(f"{website:<25} | {product:<20} | {price:<20} ")


async def fetch_price(session_url, query):
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        page: Page = await browser.new_page()
        await page.goto(session_url)

        # Fetch the data from the page
        data = await page.query_data(query)
        await browser.close()
    return data["nintendo_switch"]["price"]


async def get_price_across_websites():

    print_header()

    # Fetch prices concurrently
    bestbuy_price, nintendo_price, target_price = await asyncio.gather(
        fetch_price(BESTBUY_URL, PRODUCT_INFO_QUERY),
        fetch_price(NINETENDO_URL, PRODUCT_INFO_QUERY),
        fetch_price(TARGET_URL, PRODUCT_INFO_QUERY),
    )

    print_row("BestBuy", "Nintendo Switch", bestbuy_price)
    print_row("Nintendo site", "Nintendo Switch", nintendo_price)
    print_row("Target", "Nintendo Switch", target_price)


if __name__ == "__main__":
    asyncio.run(get_price_across_websites())
