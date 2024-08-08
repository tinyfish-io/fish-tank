"""This example demonstrates how to customize the web driver used by AgentQL."""

import agentql

# Importing the default PlaywrightWebDriver from AgentQL library
from agentql.ext.playwright.sync_api import PlaywrightWebDriver

# Set the URL to the desired website
URL = "https://www.google.com"

if __name__ == "__main__":

    # Set headless to True to hide the browser and run the script in the background
    driver = PlaywrightWebDriver(headless=True)

    # Start a session with the specified URL and the custom driver
    session = agentql.start_session(URL, web_driver=driver)

    # Define the queries to interact with the page
    QUERY = """
    {
        search_input
        search_btn
    }"""

    response = session.query(QUERY)

    # This is just to demonstrate that browser was running in the background and we get the response object successfully
    print(response.to_data())

    # Stop the session
    session.stop()
