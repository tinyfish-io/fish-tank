#!/usr/bin/env python3

"""This is an example of how to collect pricing data from e-commerce website using AgentQL."""

import asyncio

import agentql
from playwright.async_api import async_playwright

# URL of the e-commerce website
# You can replace it with any other e-commerce website but the queries should be updated accordingly
URL = "https://formsmarts.com/html-form-example"

form_text_input = {
    "first_name": "John",
    "last_name": "Doe",
    "email": "johndoe@agentql.com",
    "inquiry_text_box": "I want to learn more about AgentQL",
}

form_select_input = {
    "subject_of_inquiry": "Sales Inquiry",
}


def construct_query(form_input):
    """Construct the query string based on form_input keys."""
    fields = "\n".join(form_input.keys())
    return f"""
    {{
        {fields}
        submit_btn
    }}
    """


async def fill_form(response, form_text_input: dict):
    """Fill the form with form_text_input."""
    for key, value in form_text_input.items():
        await getattr(response, key).fill(value)


async def select_option(response, form_select_input: dict):
    """Select the form_select_input."""
    for key, value in form_select_input.items():
        print(f"Selecting {key} with value: {value}")
        await getattr(response, key).select_option(label=value)


async def main():
    """Main function."""
    async with async_playwright() as playwright, await playwright.chromium.launch(
        headless=False
    ) as browser:
        # Create a new page in the browser and wrap it to get access to the AgentQL's querying API
        page = await agentql.wrap_async(browser.new_page())
        await page.goto(URL)  # open the target URL

        form_input = {**form_text_input, **form_select_input}

        query = construct_query(form_input)
        print(f"Query: {query}")

        await page.wait_for_timeout(3000)  # wait for 3 seconds
        response = await page.query_elements(query)

        await fill_form(response, form_text_input)
        await select_option(response, form_select_input)

        await response.wait_for_timeout(3000)  # wait for 3 seconds

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
