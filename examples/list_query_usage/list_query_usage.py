import agentql
import os

# Set the URL to the desired website
URL = "https://getyourfckingsocks.com/shop"

if __name__ == "__main__":
    
    # Define the queries to interact with the page
    QUERY = """
    {
        socks[]
        {
            style_name
            price
        }
    }"""

    # Start a session with the specified URL
    session = agentql.start_session(URL)

    # Make API call(s) to AgentQL server to fetch the query
    response = session.query(QUERY)

    socks_data = response.socks.to_data()
    
    #  Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Create path to the csv file
    csv_file_path = os.path.join(script_dir, "socks_data.csv")

    # Write the data to a csv file
    with open(csv_file_path, "w") as file:
        file.write("Style Name, Price\n")
        for sock in socks_data:
            file.write(f"{sock['style_name']},{sock['price']}\n")
    

    # Stop the session
    session.stop()