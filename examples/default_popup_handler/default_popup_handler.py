"""This example demonstrates how to use the default popup handler to close all popups."""
import time
import agentql

from agentql.sync_api.web import PlaywrightWebDriver
from agentql.sync_api import close_all_popups_handler

# Set the URL to the desired website
URL = "https://bonobos.com/"

if __name__ == "__main__":
    # Set headless to False to see the browser in action
    driver = PlaywrightWebDriver(headless=False)

    # Start a session with the specified URL and the custom driver
    session = agentql.start_session(URL, web_driver=driver)

    # Define the queries to interact with the page
    QUERY = """
    {
        search_btn
    }"""

    # Use the default popup handler to close all popups
    session.on("popup", close_all_popups_handler)

    # Make API call(s) to AgentQL server to fetch the query
    response = session.query(QUERY)

    # Wait for 5 seconds to see the browser in action
    time.sleep(5)

    # Stop the session
    session.stop()