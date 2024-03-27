"""This example demonstrates how to levergae to_data() method provided by AgentQL."""
import agentql
import asyncio

# Importing the default PlaywrightWebDriver from AgentQL library
from agentql.async_api.web import PlaywrightWebDriver

# Set the URL to the desired website
AMAZON_URL = "https://www.amazon.com/Nintendo-Switch-OLED-Model-Neon-Joy/dp/B098RL6SBJ/ref=sr_1_2?crid=M1VXR6B580N1&dib=eyJ2IjoiMSJ9.SnJwwaQgWAAz2ipQdcQ--1oD_RFW8sY6H0aMKBzxU62fEEvvrjWWwIInVKw0QRI6Fr9rneWqEj5IVALwzoalaRjoQECDjlhSdCBv8OMJnX27l2_uIaUDVj1iq0Idz4iuxHv9FAxGUqOcIgeXMovxLr9d955NZoMr2Jm-HLEhtYx6P6es96OOMWd8y0Ufofumsilu4dp_sAyaHKAUU59ubjhN1iUFeSIaX-h_xYHLb5k.PM2S_-8ic6AIy9ooBoUCx7_3ooOZytd_8L_GOpXjRcc&dib_tag=se&keywords=nintendo+switch&qid=1708647744&sprefix=nintendo+switch%2Caps%2C308&sr=8-2" 
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
    # Set headless to False to see the browser in action
    driver = PlaywrightWebDriver(headless=False)
    session = await agentql.start_async_session(session_url, web_driver=driver)
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
    amazon_price, nintendo_price, target_price = await asyncio.gather(
        fetch_price(AMAZON_URL, PRODUCT_INFO_QUERY),
        fetch_price(NINETENDO_URL, PRODUCT_INFO_QUERY),
        fetch_price(TARGET_URL, PRODUCT_INFO_QUERY)
    )

    print_row("Amazon", "Nintendo Switch", amazon_price)
    print_row("Nintendo site", "Nintendo Switch", nintendo_price)
    print_row("Target", "Nintendo Switch", target_price)

if __name__ == "__main__":
    asyncio.run(get_price_across_websites())