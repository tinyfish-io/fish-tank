import webql
from webql.web import PlaywrightWebDriver
import time

driver = PlaywrightWebDriver(headless=False)

session = webql.start_session("http://lu.ma/geminimeetup", web_driver=driver)


QUERY = """
{
    event_name
    join_button
}
"""

FORM_QUERY = """
{
    name_input
    email_input
    linkedin_input
    request_to_join
    alert
}
"""


#Main Page
response = session.query(QUERY)
print(response.event_name.text_content())
response.join_button.click(force=True)

#Join Page
response = session.query(FORM_QUERY)
response.name_input.type("Justin Woo")
response.email_input.type("justinteachesai@gmail.com")
response.linkedin_input.type('https://linkedin.com/in/justinzw')

response.request_to_join.click(force=True)

time.sleep(3000)

session.stop()
