import webql
import time
import logging
from webql.sync_api.web import PlaywrightWebDriver


logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)


URL = "https://www.nike.com/w/mens-best-76m50znik1"

driver = PlaywrightWebDriver(headless=False)

session = webql.start_session(URL, web_driver=driver)

QUERY = """
{
    shoes[]{
        title
        price
        colors
    }
    
}
"""
response = session.query(QUERY)
data = response.shoes.to_data()

#Full page screenshot is a screenshot of a full scrollable page, as if you had a very tall screen and the page could fit it entirely.
#Documentation: https://playwright.dev/docs/screenshots#full-page-screenshots

driver.get_current_page().screenshot(
            path="fullpage.png", full_page=True
        )

print(data)

session.stop()
