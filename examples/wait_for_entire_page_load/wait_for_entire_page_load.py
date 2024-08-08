"""This example demonstrates how to wait for the page to load completely before querying the page."""

from agentql.ext.playwright.sync_api import Page
from playwright.sync_api import sync_playwright

# Yotube video URL to demonstrate the example for loading comments on the video
URL = "https://www.youtube.com/watch?v=F6hmwkI3n64"

QUERY = """
{
    comments[] {
        comment_content
        author
        date
    }
}
"""


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        # Create a new AgentQL page instance in the browser for web interactions
        page: Page = browser.new_page()
        page.goto(URL)

        for _ in range(3):
            # Wait for the page to load (helps to load the comments on the video)
            page.wait_for_page_ready_state()
            # Scroll down the page to trigger loading of comments
            page.keyboard.press("PageDown")

        response = page.query_data(QUERY)

        # Print the first comment
        print(response["comments"][0])

        browser.close()


if __name__ == "__main__":
    main()
