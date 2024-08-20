#!/usr/bin/env python3

"""This is an example of how to collect pricing data from e-commerce website using AgentQL."""

import asyncio

import agentql
from agentql.ext.playwright.async_api import Page
from playwright.async_api import async_playwright

# URL of the e-commerce website
# You can replace it with any other e-commerce website but the queries should be updated accordingly
URL = "https://www.bestbuy.com"


async def _do_extract_pricing_data(page: Page) -> list:
    """Extract pricing data from the current page.

    Args:
        page (Page): The Playwright page object to interact with the browser.

    Returns:
        list: The pricing data extracted from the page.
    """
    # The query of the data to be extracted
    query = """
    {
        products[] {
            name
            model
            sku
            price
        }
    }"""
    pricing_data = await page.query_data(query)

    return pricing_data.get("products", [])


async def _search_product(
    page: Page,
    product: str,
    min_price: int,
    max_price: int,
) -> bool:
    """Search for a product with a price range.

    Args:
        page (Page): The Playwright page object to interact with the browser.
        product (str): The product name to search for.
        min_price (int): The minimum price of the product.
        max_price (int): The maximum price of the product.

    Returns:
        bool: True if the search is successful, False otherwise.
    """

    # Search for a product
    search_input = await page.get_by_prompt("the search input field")
    if not search_input:
        print("Search input field not found.")
        return False
    await search_input.type(product, delay=200)
    await search_input.press("Enter")

    # Define price range
    min_price_input = await page.get_by_prompt("the min price input field")
    if not min_price_input:
        print("Min price input field not found.")
        return False
    await min_price_input.fill(str(min_price))

    max_price_input = await page.get_by_prompt("the max price input field")
    if not max_price_input:
        print("Max price input field not found.")
        return False
    await max_price_input.fill(str(max_price))
    await max_price_input.press("Enter")
    return True


async def _go_to_the_next_page(page: Page) -> bool:
    """Navigate to the next page of the search results.

    Args:
        page (Page): The Playwright page object to interact with the browser.

    Returns:
        bool: True if the next page is navigated successfully, False if no more next page.
    """
    # Find the next page button using smart locator
    next_page_query = """
    {
        pagination {
            prev_page_url
            next_page_url
        }
    }"""
    print("Navigating to the next page...")
    pagination = await page.query_data(next_page_query)
    next_page_url = pagination.get("pagination", {}).get("next_page_url")
    if not next_page_url:
        return False
    try:
        if not next_page_url.startswith("http"):
            next_page_url = URL + next_page_url  # Make it a full URL
        await page.goto(next_page_url)
        return True
    except Exception:
        pass

    return False


async def extract_pricing_data(
    page: Page,
    product: str,
    min_price: int,
    max_price: int,
    max_pages: int = 3,
) -> list:
    """Extract pricing data for a product within a price range."""
    # Search for the product with the specified price range
    print(f"Searching for product: {product} with price range: ${min_price} - ${max_price}")
    if await _search_product(page, product, min_price, max_price) is False:
        print("Failed to search for the product.")
        return []

    current_page = 1
    pricing_data = []
    while current_page <= max_pages:
        # Extract pricing data from the current page
        print(f"Extracting pricing data on page {current_page}...")
        pricing_data_on_page = await _do_extract_pricing_data(page)
        print(f"{len(pricing_data_on_page)} products found")

        pricing_data.extend(pricing_data_on_page)

        # Navigate to the next page
        if not await _go_to_the_next_page(page):
            print("No more next page.")
            break

        current_page += 1

    return pricing_data


async def main():
    """Main function."""
    async with async_playwright() as playwright, await playwright.chromium.launch(
        headless=False
    ) as browser:
        # Create a new page in the browser and wrap it to get access to the AgentQL's querying API
        page = await agentql.wrap_async(browser.new_page())
        await page.goto(URL)  # open the target URL

        pricing_data = await extract_pricing_data(
            page,
            product="gpu",
            min_price=500,
            max_price=800,
        )

        print(pricing_data)


if __name__ == "__main__":
    asyncio.run(main())
