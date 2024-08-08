""""This is an example of how to use AgentQL to track the cheapest flight price from Skyscanner website."""

import agentql
from agentql.sync_api import ScrollDirection

# Set the URL to the desired website (Skyscanner in this case)
URL = "https://www.skyscanner.co.in/"

# Set the device information to prevent bot detection by the website )
# These device information can be obtained from browser fingerprinting websites such as https://bot.sannysoft.com/ and https://pixelscan.net/
VENDOR_INFO = "Google Inc. (Apple)"
RENDERER_INFO = "ANGLE (Apple, Apple M3 Max, OpenGL 4.2)"
USER_AGENT_INFO = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"

if __name__ == "__main__":

    # Start a session with the specified URL
    session = agentql.start_session(URL)

    # Enable stealth mode to prevent bot detection by the website
    session.driver.enable_stealth_mode(
        webgl_vendor=VENDOR_INFO,
        webgl_renderer=RENDERER_INFO,
        nav_user_agent=USER_AGENT_INFO,
    )

    # Define the queries to interact with the page (You could tweak the queries as per item you want to track on the website)
    QUERY_1 = """
    {
        depart_airpot
        arrival_airport
        depart_date_picker
    }
    """

    # Make API call(s) to AgentQL server to fetch the query
    response_1 = session.query(QUERY_1)

    response_1.depart_airpot.fill("AMD")

    QUERY_2 = """
    {
        ahmedabad
    }
    """

    response_2 = session.query(QUERY_2)

    response_2.ahmedabad.click(force=True)

    QUERY_3 = """
    {
        destination_airport
    }
    """

    response_3 = session.query(QUERY_3)

    response_3.destination_airport.fill("PNQ")

    QUERY_4 = """
    {
        pune
    }
    """

    response_4 = session.query(QUERY_4)

    response_4.pune.click(force=True)

    QUERY_5 = """
    {
        depart_date_picker
    }
    """

    response_5 = session.query(QUERY_5)

    response_5.depart_date_picker.click(force=True)

    DATE_QUERY = """
    {
        random_available_date_btn
    }
    """

    response_date = session.query(DATE_QUERY)

    response_date.random_available_date_btn.click(force=True)

    SEARCH_QUERY = """
    {
        search_btn
    }
    """

    response_search = session.query(SEARCH_QUERY)

    response_search.search_btn.click(force=True)

    QUERY_6 = """
    {
        apply_btn
    }
    """

    response_6 = session.query(QUERY_6)

    # Scroll the page to click on the apply button
    session.driver.scroll_page(ScrollDirection.DOWN)

    response_6.apply_btn.click(force=True)

    # Wait for the page to load (helps to load the flight details)
    session.driver.wait_for_page_ready_state()

    QUERY_7 = """
    {
        flight {
            cheapest_price
        }
    }"""

    response_7 = session.query(QUERY_7)

    # This will print the cheapest flight price
    print(response_7.flight.to_data())

    # Stop the session
    session.stop()
