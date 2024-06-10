"""This example demonstrates how to levergae to_data() method provided by AgentQL."""
import agentql
import asyncio

# Set the URL to the desired website
WALMART_URL = "https://www.walmart.com/ip/Nintendo-Switch-OLED-Model-w-White-Joy-Con/910582148?athbdg=L1600"
TARGET_URL = "https://www.target.com/p/nintendo-switch-oled-model-with-white-joy-con/-/A-83887639#lnk=sametab"
NINETENDO_URL = "https://www.nintendo.com/us/store/products/nintendo-switch-oled-model-white-set/"

def print_header():
    """Prints the header for the data table"""
    print(f"{'Website':<25} | {'Product ':<20} | {'Price ':<20} ")
    print("-" * 75)

def print_row(website, product, price):
    """Prints the data row"""
    print(f"{website:<25} | {product:<20} | {price:<20} ")

async def fetch_price(session_url, query):
    session = await agentql.start_async_session(session_url)
    await session.driver.wait_for_page_ready_state()
    response = await session.query(query)
    data = await response.nintendo_switch.to_data()
    await session.stop()
    return data["price"]

async def get_price_across_websites():
    

    # Define the queries to interact with the page
    PRODUCT_INFO_QUERY = """
    {
        nintendo_switch
        {
            price
        }
    }"""

    print_header()

    # Fetch prices concurrently
    walmart_price, nintendo_price, target_price = await asyncio.gather(
        fetch_price(WALMART_URL, PRODUCT_INFO_QUERY),
        fetch_price(NINETENDO_URL, PRODUCT_INFO_QUERY),
        fetch_price(TARGET_URL, PRODUCT_INFO_QUERY)
    )

    print_row("Walmart", "Nintendo Switch", walmart_price)
    print_row("Nintendo site", "Nintendo Switch", nintendo_price)
    print_row("Target", "Nintendo Switch", target_price)

if __name__ == "__main__":
    asyncio.run(get_price_across_websites())