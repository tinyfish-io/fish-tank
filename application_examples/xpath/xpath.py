import agentql

#import https://pypi.org/project/playwright-dompath/ 
# Playwright Dompath is a Python library that helps you to generate XPath from Playwright selectors.
from playwright_dompath.dompath_sync import xpath_path

session = agentql.start_session("https://www.google.com")

QUERY = """
{
    search_box
    search_btn
    about_link
}
"""

response = session.query(QUERY)

print(response.about_link.text_content())

# Get the XPath 
print("XPath:", xpath_path(response.search_btn))

response.search_box.fill("tinyfish")
response.search_btn.click(force=True)


session.stop()

