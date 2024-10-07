import logging

import agentql
from playwright.sync_api import sync_playwright

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)


if __name__ == "__main__":
    QUERY = """
    {
        page_title
        post_headers[]
    }
    """
    with sync_playwright() as playwright, playwright.chromium.launch(headless=False) as browser:
        page = agentql.wrap(browser.new_page())

        log.info("Navigating to the page...")

        page.goto("https://infinite-scroll.com/demo/full-page/")
        page.wait_for_page_ready_state()

        num_extra_pages_to_load = 3

        for times in range(num_extra_pages_to_load):
            log.info(f"Scrolling to the bottom of the page... (num_times = {times+1})")
            page.keyboard.press("End")
            page.wait_for_page_ready_state()
            log.info("Content loaded!")

        log.info("Issuing AgentQL data query...")
        response = page.query_data(QUERY)

        log.info(f"AgentQL response: {response}")
