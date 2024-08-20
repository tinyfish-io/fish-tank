"""This example demonstrates how to query a list of items on the page."""

import os

import agentql
from playwright.sync_api import sync_playwright

# Set the URL to the desired website
URL = "https://getyourfckingsocks.com/shop"

# Define the queries to interact with the page
QUERY = """
{
    socks[]
    {
        style_name
        price
    }
}
"""


def main():
    with sync_playwright() as playwright, playwright.chromium.launch(headless=False) as browser:
        # Create a new page in the browser and wrap it to get access to the AgentQL's querying API
        page = agentql.wrap(browser.new_page())

        page.goto(URL)

        # Use query_data() method to fetch the data from the page
        response = page.query_data(QUERY)

        #  Get the directory of the current script
        script_dir = os.path.dirname(os.path.abspath(__file__))

        # Create path to the csv file
        csv_file_path = os.path.join(script_dir, "socks_data.csv")

        # Write the data to a csv file
        with open(csv_file_path, "w", encoding="utf-8") as file:
            file.write("Style Name, Price\n")
            for sock in response["socks"]:
                file.write(f"{sock['style_name']},{sock['price']}\n")


if __name__ == "__main__":
    main()
