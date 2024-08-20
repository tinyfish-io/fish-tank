"""This example demonstrates how to perform sentiment analysis on YouTube comments with AgentQL and OpenAI's GPT-3.5 model."""

import os

import agentql
from openai import OpenAI
from playwright.sync_api import sync_playwright

URL = "https://www.youtube.com/watch?v=JfM1mr2bCuk"

# Define the queries to interact with the page
QUERY = """
{
    video_title
    video_channel
    comments[] {
        comment_text
        author
    }
}
"""


def get_comments():
    with sync_playwright() as playwright, playwright.chromium.launch(headless=False) as browser:
        # Create a new page in the browser and wrap it to get access to the AgentQL's querying API
        page = agentql.wrap(browser.new_page())

        page.goto(URL)

        for _ in range(5):
            # Wait for the page to load (helps to load the comments on the video)
            page.wait_for_page_ready_state()

            # Scroll down the page to load more comments
            page.keyboard.press("PageDown")

        # Use query_data() method to fetch the comments from the page
        response = page.query_data(QUERY)

        return response


def perform_sentiment_analysis(comments):
    USER_MESSAGE = "These are the comments on the video. I am trying to understand the sentiment of the comments."

    for comment in comments["comments"]:
        USER_MESSAGE += comment["comment_text"]

    SYSTEM_MESSAGE = """You are an expert in understanding the social media analytics and analysis and specialize in analyzing sentiment of the comments.
    Please find the comments on the video as follows:

    """

    USER_MESSAGE += "Could you please provide a summary of the comments on the video. Additionaly, just give only 3 takeaways which would be important for me as the creator of the video."

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": SYSTEM_MESSAGE},
            {"role": "user", "content": USER_MESSAGE},
        ],
    )

    return completion.choices[0].message.content


def main():
    comments = get_comments()
    summary = perform_sentiment_analysis(comments)
    print(summary)


if __name__ == "__main__":
    main()
