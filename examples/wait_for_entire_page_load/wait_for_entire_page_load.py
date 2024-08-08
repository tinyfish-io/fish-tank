"""This example demonstrates how to wait for the page to load completely before querying the page."""

from agentql.ext.playwright.sync_api import Page
from playwright.sync_api import sync_playwright

# Yotube video URL to demonstrate the example for loading comments on the video
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
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        # Create a new AgentQL page instance in the browser for web interactions
        page: Page = browser.new_page()
        page.goto(URL)

        for _ in range(2):
            # Wait for the page to load (helps to load the additional videos)
            page.wait_for_page_ready_state()
            # Scroll down the page to trigger loading of more videos
            page.keyboard.press("End")

        response = page.query_data(QUERY)

        # Print the first video details
        print(response["videos"][0])

        browser.close()


if __name__ == "__main__":
    main()
