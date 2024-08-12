""""This example demonstrates how to save and load the user session state using AgentQL."""

import json
import os
import time

import agentql

# Set the URL to the desired website
URL = "https://www.instagram.com"

# Set the user_id and password for the website
URL_USER_ID = "#Insert your user_id for the website here"
URL_PASSWORD = "#Insert your password for the website here"


def get_user_session_state():

    # Start a session with the specified URL
    session = agentql.start_session(URL)

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

    user_session = session.get_user_auth_session()

    # Save the user session state to a file
    with open("user_session_instagram.json", "w", encoding="utf-8") as file:
        file.write(json.dumps(user_session))

    session.stop()

    return user_session


if __name__ == "__main__":

    if os.path.exists("user_session_instagram.json"):
        with open("user_session_instagram.json", "r", encoding="utf-8") as file:
            content = file.read()
            user_session = json.loads(content)

    else:
        get_user_session_state()

        with open("user_session_instagram.json", "r", encoding="utf-8") as file:
            content = file.read()
            user_session = json.loads(content)

    # Start a session with the specified URL
    session = agentql.start_session(URL, user_auth_session=user_session)

    # Wait for 5 seconds to see the browser in action
    time.sleep(5)
