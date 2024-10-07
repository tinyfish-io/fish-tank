#!/usr/bin/env python3

"""This is an example of how to collect pricing data from e-commerce website using AgentQL."""

import asyncio

import agentql
from playwright.async_api import async_playwright

# URL of the e-commerce website
# You can replace it with any other e-commerce website but the queries should be updated accordingly
URL = "https://formsmarts.com/html-form-example"


async def main():
    """Main function."""
    async with async_playwright() as playwright, await playwright.chromium.launch(
        headless=False
    ) as browser:
        # Create a new page in the browser and wrap it to get access to the AgentQL's querying API
        page = await agentql.wrap_async(browser.new_page())
        await page.goto(URL)  # open the target URL

        form_query = """
        {
            first_name
            last_name
            email
            subject_of_inquiry
            inquiry_text_box
            submit_btn
        }
        """
        response = await page.query_elements(form_query)

        await response.first_name.fill("John")
        await response.last_name.fill("Doe")
        await response.email.fill("johndoe@agentql.com")
        await response.subject_of_inquiry.select_option(label="Sales Inquiry")
        await response.inquiry_text_box.fill("I want to learn more about AgentQL")

        # Submit the form
        await response.submit_btn.click()

        # confirm form
        confirm_query = """
        {
            confirmation_btn
        }
        """

        response = await page.query_elements(confirm_query)
        await response.confirmation_btn.click()
        await page.wait_for_page_ready_state()
        await page.wait_for_timeout(3000)  # wait for 3 seconds
        print("Form submitted successfully!")


if __name__ == "__main__":
    asyncio.run(main())
