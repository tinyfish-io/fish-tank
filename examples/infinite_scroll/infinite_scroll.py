import logging
import random
import time

import agentql
from agentql.ext.playwright.sync_api import Page
from playwright.sync_api import sync_playwright

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)


def key_press_end_scroll(page: Page):
    page.keyboard.press("End")


def mouse_wheel_scroll(page: Page):
    viewport_height, total_height, scroll_height = page.evaluate(
        "() => [window.innerHeight, document.body.scrollHeight, window.scrollY]"
    )
    while scroll_height < total_height:
        scroll_height = scroll_height + viewport_height
        page.mouse.wheel(delta_x=0, delta_y=viewport_height)
        time.sleep(random.uniform(0.05, 0.1))


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
            key_press_end_scroll(page)
            page.wait_for_page_ready_state()
            log.info("Content loaded!")

        log.info("Issuing AgentQL data query...")
        response = page.query_data(QUERY)

        log.info(f"AgentQL response: {response}")
