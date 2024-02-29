"""This example demonstrates how to use the default popup handler to close all popups."""
import time
import webql

from webql.sync_api.web import PlaywrightWebDriver
from webql.sync_api import close_all_popups_handler

# Set the URL to the desired website
URL = "https://partakefoods.com/"

if __name__ == "__main__":
    # Set headless to False to see the browser in action
    driver = PlaywrightWebDriver(headless=False)

    # Start a session with the specified URL and the custom driver
    session = webql.start_session(URL, web_driver=driver)

    # Define the queries to interact with the page
    QUERY = """
    {
        search_btn
    }"""

    # Use the default popup handler to close all popups
    session.on("popup", close_all_popups_handler)

    # Make API call(s) to AgentQL server to fetch the query
    response = session.query(QUERY)

    # Wait for 2 seconds to see the browser in action
    time.sleep(2)

    # Stop the session
    session.stop()