"""This example demonstrates how to wait for the page to load completely before querying the page."""

from agentql.ext.playwright.sync_api import Page
from playwright.sync_api import sync_playwright

# Duckduckgo URL to demonstrate the example for loading more videos on the page
URL = "https://duckduckgo.com/?q=machine+learning+lectures+mit&t=h_&iar=videos&iax=videos&ia=videos"

QUERY = """
{
    videos(first 10 videos)[] {
        video_title
        length
        views
    }
}
"""


def main():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)

        # Create a new page in the browser and cast it to custom Page type to get access to the AgentQL's querying API
        page: Page = browser.new_page()  # type: ignore

        page.goto(URL)

        for _ in range(2):
            # Wait for additional videos to load completely
            page.wait_for_page_ready_state()
            # Scroll down the page to trigger loading of more videos
            page.keyboard.press("End")

        # # Use query_data() method to fetch video lists data from the page
        response = page.query_data(QUERY)

        # Print the details of the first video
        print(response["videos"][0])

        browser.close()


if __name__ == "__main__":
    main()
