import logging
import time

import webql
from webql.web import PlaywrightWebDriver

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)
URL = "https://www.youtube.com/"

if __name__ == "__main__":
    driver = PlaywrightWebDriver(headless=False)
    session = webql.start_session(URL, web_driver=driver)

    SEARCH_QUERY = """
    {
        search_input
        search_button
    }"""

    VIDEO_QUERY = """
    {
        videos[] { 
            video_link
            video_title
            channel_name
        }
    }
    """

    SKIP_QUERRY = """
    {
        skip_button
    }
    """

    try:
    # search query
        response = session.query(SEARCH_QUERY)
        response.search_input.type("1 hour force awakens", delay=75)
        response.search_button.click()

    # video query
        response = session.query(VIDEO_QUERY)
        log.debug(f"Clicking Youtube Video: {response.videos[0].video_title.text_content()}")
        response.videos[0].video_link.click()  # click the first youtube video

    #wait for skip button to show up
        
        time.sleep(8)

        response = session.query(SKIP_QUERRY)
        response.skip_button.click()

    except Exception as e:
        log.error(f"Found Error: {e}")
    raise e

    time.sleep(3)
    #session.stop()
