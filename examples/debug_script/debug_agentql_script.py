import logging

import agentql
from agentql.sync_api import DebugManager

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)


if __name__ == "__main__":
    # The following context manager will enable debug mode for the script.
    with DebugManager.debug_mode():
        session = agentql.start_session("https://www.google.com")

        # Define the queries to interact with the page
        QUERY = """
            {
                search_box
                search_btn
                about_link
            }
            """

        response = session.query(QUERY)

        # Buggy code that will crash the script. When it crashes, the debug manager will save debug files to designated directory (~/.agentql/debug by default).
        response.search.fill("tinyfish")
        response.search_btn.click(force=True)

        session.stop()
        log.debug(session.get_last_trail())
