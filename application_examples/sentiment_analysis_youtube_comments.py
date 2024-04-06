from openai import OpenAI
import agentql

URL = "https://www.youtube.com/watch?v=JfM1mr2bCuk"

if __name__ == "__main__":

    # Start a session with the specified URL and the custom driver
    session = agentql.start_session(URL)

    driver = session.driver

    # (Note: The current script is configured to load about 100 comments on the video)
    for i in range(5):
        #  Each Scroll will load about 20 comments on the video
        driver.scroll_to_bottom()

        # Wait for the page to load (helps to load the comments on the video)
        driver.wait_for_page_ready_state()
    
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

    # Make API call(s) to AgentQL server to fetch the query
    response = session.query(QUERY)

    # Leveraging to_data() method to extract the comments data from the response
    comments_data_json = response.comments.to_data()

    # Stop the session
    session.stop()

    # Leveraging OpenAI's GPT-3.5 model to understand the sentiment of the comments
    client = OpenAI()

    USER_MESSAGE = "These are the comments on the video. I am trying to understand the sentiment of the comments."

    for comment in comments_data_json:
        USER_MESSAGE += comment["comment_text"]


    SYSTEM_MESSAGE = """You are an expert in understanding the social media analytics and analysis and specialize in analyzing sentiment of the comments. 
    Please find the comments on the video as follows:
    
    """
    
    USER_MESSAGE += "Could you please provide a summary of the comments on the video. Additionaly, just give only 3 takeaways which would be important for me as the creator of the video."

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            { "role": "system", "content": SYSTEM_MESSAGE },
            { "role": "user", "content": USER_MESSAGE },
        ]
    )

    # Print the response from the GPT-3.5 model (Sentiment Analysis of the comments on the video)
    print(completion.choices[0].message.content)

    