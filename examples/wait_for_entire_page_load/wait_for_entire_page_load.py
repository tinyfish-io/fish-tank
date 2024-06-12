"""This example demonstrates how to wait for the page to load before querying the page and levergae scroll method."""
import agentql

# Yotube video URL to demonstrate the example for loading comments on the video
URL = "https://www.youtube.com/watch?v=F6hmwkI3n64"

if __name__ == "__main__":
    
    # Start a session with the specified URL and the custom driver
    session = agentql.start_session(URL)

    # (Note: The current script is configured to load about 100 comments on the video)
    for i in range(5):
        #  Each Scroll will load about 20 comments on the video
        session.driver.scroll_to_bottom()

        # Wait for the page to load (helps to load the comments on the video)
        session.driver.wait_for_page_ready_state()

    QUERY = """
    {
        comments[] {
            comment_title
            author
            date
        }
    }
    """

    response = session.query(QUERY)

    # TODO: Add appropriate code for consumtpion of the comments data
    # Example: Levergae AgentQL's to_data() method to extract the content of comments and do sentiment analysis of the comments on the video
    print(response.to_data())
    session.stop()
