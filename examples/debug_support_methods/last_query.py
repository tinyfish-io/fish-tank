""" This example demonstrates how to use the last_query and last_response attributes of the session object to debug the queries and responses. """

import agentql

# Set the URL to the desired website
URL = "https://www.badmintonwarehouse.com/"

if __name__ == "__main__":
    # Start a session with the specified URL
    session = agentql.start_session(URL)

    # Define the queries to interact with the page
    HOMEPAGE_QUERY = """
    {
        search_box  
        search_btn 
    }
    """

    # Fetch the response of the query
    response = session.query(HOMEPAGE_QUERY)

    response.search_box.fill("Mavis 350 Nylon Shuttlecock (Yellow/Fast)")
    response.search_btn.click(force=True)

    CHOOSE_PRODUCT_QUERY = """
    {
        products[] 
        {
            product_name
            product_link
        }
    }
    """

    response = session.query(CHOOSE_PRODUCT_QUERY)

    # Check if the search returned more than 1 product
    if len(response.products) > 1:
        print("More than 1 product found, please filter the search.")

    # Check if the search returned no products
    elif len(response.products) == 0:
        print("No products found")

    # If only 1 product is found, click on the product link
    else:
        response.products[0].product_link.click(force=True)

        PRODUCT_QUERY = """
        {
            product {
                discounted_price
            }
        }
        """

        response = session.query(PRODUCT_QUERY)

        price_string = response.product.to_data().get("discounted_price")
        price = float(price_string.replace("$", "").strip())

        # Check if prices is in the budget
        if price < 10:

            ADD_TO_CART_QUERY = """
            {
                add_to_cart_btn
            }
            """

            response = session.query(ADD_TO_CART_QUERY)

            response.add_to_cart_btn.click(force=True)

        else:
            print("Let's wait for sale, current price is too high: ", response.product.to_data())

    # We had a nested if-else based script, it is helpful to get visibility and debug based on the last executed query and response
    # We can use the last_query and last_response attributes to debug the queries and responses in the script
    print("This was the last query executed ", session.last_query)

    print("This was the last response received ", session.last_response)
