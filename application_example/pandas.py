import webql
import json
import pandas as pd
import logging
from webql.sync_api.web import PlaywrightWebDriver


logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

URL = "https://www.nike.com/w/mens-shoes-nik1zy7ok"

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

#Let's dump the data out to a json file for us to use.

with open("nike.json", "w") as outfile:
    json.dump(data, outfile)

#We use pandas to take the dictand convert it to a dataframe
df = pd.DataFrame.from_dict(data)

#This makes it super simple to print a table
print(df.to_string())

#We can even print that table to a file
with open('nikeTable.txt', 'a') as f:
    f.write(df.to_string())

session.stop()
