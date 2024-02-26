""""This example demonstrates how to save and load the user session state using AgentQL."""
import time
import webql
import os

# Importing the default PlaywrightWebDriver from AgentQL library
from webql.sync_api.web import PlaywrightWebDriver
from webql.sync_api.session import Session

# Set the URL to the desired website
URL = "https://www.instagram.com"

# Set the user_id and password for the website
URL_USER_ID = "#Insert your user_id for the website here" 
URL_PASSWORD = "#Insert your password for the website here"

def get_user_session_state():
    # Set headless to False to see the browser in action
    driver = PlaywrightWebDriver(headless=False)

    # Start a session with the specified URL and the custom driver
    session = webql.start_session(URL, web_driver=driver)

    # Define the queries to interact with the page (for login)
    QUERY = """
    {                  
        username
        password
        login_btn
    }"""

    response = session.query(QUERY)

    response.username.fill(URL_USER_ID)
    response.password.fill(URL_PASSWORD)
    response.login_btn.click(force=True)

    # Wait for 5 seconds to ensure the user session state is saved entirely
    time.sleep(5)

    # Save the user session state to a file
    session.save_user_session_state("user_session_instagram.json")

    session.stop()

if __name__ == "__main__":

    if os.path.exists('user_session_instagram.json'):
        user_session_state = Session.load_user_session_state("user_session_instagram.json")

    else:
        get_user_session_state()

        user_session_state = Session.load_user_session_state("user_session_instagram.json")
    

    # Start a new session with the user session state
    driver = PlaywrightWebDriver(headless=False)

    # Start a session with the specified URL and the custom driver and the user session state
    session = webql.start_session(URL, web_driver=driver, storage_state=user_session_state)

    # Wait for 5 seconds to see the browser in action
    time.sleep(5)

