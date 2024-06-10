import asyncio
import logging

import agentql
from agentql.async_api import DebugManager

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)


async def main():
    # The following async context manager will enable debug mode for the script.
    async with DebugManager.debug_mode():
        session = await agentql.start_async_session("https://www.google.com")

        # Define the queries to interact with the page
        QUERY = """
        {
            search_box
            search_btn
            about_link
        }
        """

        response = await session.query(QUERY)

        # Buggy code that will crash the script. When it crashes, the debug manager will save debug files to designated directory (~/.agentql/debug by default).
        await response.search.type("Tinyfish")
        await response.search_btn.click()

        await session.stop()


if __name__ == "__main__":
    asyncio.run(main())
