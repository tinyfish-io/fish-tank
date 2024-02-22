import time
import webql
from webql.sync_api.web import PlaywrightWebDriver

URL = "https://www.target.com"
EMAIL = "REPLACE_WITH_YOUR_EMAIL (For target.com)"
PASSWORD = "REPLACE_WITH_YOUR_PASSWORD (For target.com)"

if __name__ == "__main__":

    # Set headless to False to see the browser in action
    driver = PlaywrightWebDriver(headless=False)

    # Start a session with the specified URL and the custom driver
    session = webql.start_session(URL, web_driver=driver)

    # Define the queries to interact with the page
    sign_in_query = """
    {
        sign_in_btn
    }
    """

    credentials_query = """
    {
        email_input
        password_input
        sign_in_with_password_btn
    }
    """

    skip_query = """
    {
        skip_btn
    }
    """

    # Make API call(s) to AgentQL server to fetch the query
    response = session.query(sign_in_query)

    response.sign_in_btn.click(force=True)

    response_sign_in = session.query(sign_in_query)

    response_sign_in.sign_in_btn.click(force=True)


    response_credentials = session.query(credentials_query)

    response_credentials.email_input.fill(EMAIL)
    response_credentials.password_input.fill(PASSWORD)
    response_credentials.sign_in_with_password_btn.click(force=True)

    response_skip = session.query(skip_query)

    response_skip.skip_btn.click(force=True)

    response_skip_promos = session.query(skip_query)

    response_skip_promos.skip_btn.click(force=True)

    # Wait for 5 seconds to see the browser in action
    time.sleep(5)
