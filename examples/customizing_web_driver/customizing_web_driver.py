"""This example demonstrates how to customize the web driver used by AgentQL."""
import time
import webql

# Importing the default PlaywrightWebDriver from AgentQL library
from webql.sync_api.web import PlaywrightWebDriver

# Set the URL to the desired website
URL = "https://www.google.com"

if __name__ == "__main__":

    # Set headless to False to see the browser in action
    driver = PlaywrightWebDriver(headless=False)

    # Start a session with the specified URL and the custom driver
    session = webql.start_session(URL, web_driver=driver)

    # Wait for 5 seconds to see the browser in action
    time.sleep(5)

