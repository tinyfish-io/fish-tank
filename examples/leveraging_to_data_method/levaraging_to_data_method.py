"""This example demonstrates how to leverage to_data() method provided by AgentQL."""
import agentql

# Set the URL to the desired website
URL = "https://www.marketwatch.com/investing/stock/googl?mod=search_symbol"

if __name__ == "__main__":

    # Define the queries to interact with the page
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
    session = agentql.start_session(URL)

    # Make API call(s) to AgentQL server to fetch the query
    response = session.query(QUERY)

    # Leveraging to_data() method to extract the data from the response
    data = response.stock_info.to_data()

    print(data)

    # Stop the session
    session.stop()