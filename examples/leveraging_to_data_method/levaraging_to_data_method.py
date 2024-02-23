"""This example demonstrates how to leverage to_data() method provided by AgentQL."""
import webql

# Importing the default PlaywrightWebDriver from AgentQL library
from webql.sync_api.web import PlaywrightWebDriver

# Set the URL to the desired website
URL = "https://www.marketwatch.com/investing/stock/googl?mod=search_symbol"

if __name__ == "__main__":

    # Set headless to False to see the browser in action
    driver = PlaywrightWebDriver(headless=False)

    QUERY = """
    {
        stock_info
        {
            price
            change
            change_percent
            market_cap
            volume
        }
    }"""

    # Start a session with the specified URL and the custom driver
    session = webql.start_session(URL, web_driver=driver)

    # Make API call(s) to AgentQL server to fetch the query
    response = session.query(QUERY)

    # Leveraging to_data() method to extract the data from the response
    data = response.stock_info.to_data()

    print(data)

    # Stop the session
    session.stop()