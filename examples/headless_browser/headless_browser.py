"""This example demonstrates how to work with default web driver configuration (headless) used by AgentQL."""
import agentql

# Set the URL to the desired website
URL = "https://google.com"

if __name__ == "__main__":

    QUERY = """
    {
        search_input
        search_btn
    }"""
    
    # Start a session with the specified URL and the custom driver
    session = agentql.start_session(URL)

    response = session.query(QUERY)

    response.search_input.fill("President of United States")

    response.search_btn.click(force=True)

    QUERY = """
    {
        urls[]
        {
            link
        }
    }"""

    response = session.query(QUERY)

    print(response)


