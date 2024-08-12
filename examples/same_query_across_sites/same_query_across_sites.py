"""This example demonstrates how to levergae to_data() method provided by AgentQL."""

import agentql

# Set the URL to the desired website
WALMART_URL = (
    "https://www.walmart.com/ip/Nintendo-Switch-OLED-Model-w-White-Joy-Con/910582148?athbdg=L1600"
)
TARGET_URL = "https://www.target.com/p/nintendo-switch-oled-model-with-white-joy-con/-/A-83887639#lnk=sametab"
NINETENDO_URL = "https://www.nintendo.com/us/store/products/nintendo-switch-oled-model-white-set/"


def print_header():
    """Prints the header for the data table"""
    print(f"{'Website':<25} | {'Product ':<20} | {'Price ':<20} ")
    print("-" * 75)


def print_row(website, product, price):
    """Prints the data row"""
    print(f"{website:<25} | {product:<20} | {price:<20} ")


if __name__ == "__main__":

    # Define the queries to interact with the page
    PRODUCT_INFO_QUERY = """
    {
        nintendo_switch
        {
            price
        }
    }"""

    print_header()

    # Start a session with the specified URL and the custom driver
    session = agentql.start_session(WALMART_URL)

    # Make API call(s) to AgentQL server to fetch the query
    response = session.query(PRODUCT_INFO_QUERY)

    # Leveraging to_data() method to extract the data from the response
    data = response.nintendo_switch.to_data()

    print_row("Walmart", "Nintendo Switch", data["price"])

    # Stop the session
    session.stop()

    # Start a session with the new URL and the same driver
    session = agentql.start_session(NINETENDO_URL)

    # Reuse the same query to fetch the data from the new website
    response = session.query(PRODUCT_INFO_QUERY)

    data = response.nintendo_switch.to_data()

    print_row("Nintendo site", "Nintendo Switch", data["price"])

    # Stop the session
    session.stop()

    # Repeat the same process for other websites
    session = agentql.start_session(TARGET_URL)

    response = session.query(PRODUCT_INFO_QUERY)

    data = response.nintendo_switch.to_data()

    print_row("Target", "Nintendo Switch", data["price"])

    session.stop()
