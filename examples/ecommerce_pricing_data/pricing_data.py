#!/usr/bin/env python3

"""This is an example of how to collect pricing data from ecommerce website using AgentQL.
"""

import asyncio
import agentql
from agentql.async_api import Session

# URL of the ecommerce website
# You can replace it with any other ecommerce website but the queries should be updated accordingly
URL = "https://www.bestbuy.com"


async def _do_extract_pricing_data(session: Session) -> list:
    """Extract pricing data from the current page.

    Args:
        session (Session): The AgentQL session object to interact with the browser.

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
    pricing_data = await session.query_data(query)
    pricing_data = await pricing_data.to_data()

    return pricing_data.get("products", [])


async def _search_product(
    session: Session,
    product: str,
    min_price: int,
    max_price: int,
):
    """Search for a product with a price range.

    Args:
        session (Session): The AgentQL session object to interact with the browser.
        product (str): The product name to search for.
        min_price (int): The minimum price of the product.
        max_price (int): The maximum price of the product.
    """

    # Find the search field using smart locator
    search_input_query = """
    {
        search_input
    }"""

    response = await session.query(search_input_query)
    await response.search_input.type(product, delay=200)
    await response.search_input.press("Enter")

    # Wait for the search result to load
    await session.driver.wait_for_page_ready_state()

    # Define price range
    price_range_query = """
    {
        min_price_input
        max_price_input
    }"""

    response = await session.query(price_range_query)
    await response.min_price_input.fill(str(min_price))
    await response.max_price_input.fill(str(max_price))
    await response.max_price_input.press("Enter")

    # Wait for the search result to update
    await session.driver.wait_for_page_ready_state()


async def _go_to_the_next_page(session: Session) -> bool:
    """Navigate to the next page of the search results.

    Args:
        session (Session): The AgentQL session object to interact with the browser.

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
    response = await session.query_data(next_page_query)
    pagination = await response.to_data()
    next_page_url = pagination.get("pagination", {}).get("next_page_url")
    if not next_page_url:
        return False
    try:
        if not next_page_url.startswith("http"):
            next_page_url = URL + next_page_url  # Make it a full URL
        await session.driver.open_url(next_page_url)
        await session.driver.wait_for_page_ready_state()
        return True
    except Exception:
        pass

    return False


async def extract_pricing_data(
    product: str,
    min_price: int,
    max_price: int,
    max_pages: int = 3,
) -> list:
    """Extract pricing data for a product within a price range."""

    # Start an async browser session with the specified URL
    session = await agentql.start_async_session(URL)

    # Search for the product with the specified price range
    print(
        f"Searching for product: ${product} with price range: ${min_price} - ${max_price}"
    )
    await _search_product(session, product, min_price, max_price)

    current_page = 1
    pricing_data = []
    while current_page <= max_pages:
        # Extract pricing data from the current page
        print(f"Extracting pricing data on page {current_page}...")
        pricing_data_on_page = await _do_extract_pricing_data(session)
        print(f"{len(pricing_data_on_page)} pricing data found")

        pricing_data.extend(pricing_data_on_page)

        # Navigate to the next page
        if not await _go_to_the_next_page(session):
            print("No more next page.")
            break

        current_page += 1

    # Stop the browser session
    await session.stop()

    return pricing_data


if __name__ == "__main__":
    # Define the product and price range to search for
    PRODUCT = "gpu"
    MIN_PRICE = 500
    MAX_PRICE = 800

    # Extract pricing data for the product within the price range
    pricing_data = asyncio.run(extract_pricing_data(PRODUCT, MIN_PRICE, MAX_PRICE))

    print(pricing_data)
