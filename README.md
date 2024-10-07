# AgentQL examples and tutorials

## Get started with AgentQL

You will need your [API Key](https://dev.agentql.com/) and the [AgentQL SDK](https://docs.agentql.com/installation/sdk-installation). You can get set up in less than five minutes with the [AgentQL Quick Start](https://docs.agentql.com/quick-start).

## Virtual Environment

This project uses [Poetry](https://python-poetry.org/docs/) for dependency and virtual environment management.
You don't have to use Poetry to run the examples, but it will make it easier to manage dependencies and isolate the project environment.
If you choose to use Poetry follow these simple steps to get everything setup:

- **Install Poetry**. Follow [Poetry official guidelines here](https://python-poetry.org/docs/#installing-with-the-official-installer)
- **Install dependencies**. Run `poetry install` in the project root directory
- **Activate the virtual environment**. Run `poetry shell` to activate the virtual environment

## Examples

This list contains basic use case examples that demonstrate the fundamental functionalities of AgentQL. It’s a great starting point for those new to AgentQL or looking to understand its core capabilities.

| Topic                                            | URL                                                                                                                                                     |
| ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Getting started with AgentQL                     | [first_step](https://github.com/tinyfish-io/fish-tank/tree/main/examples/first_steps)                                                                   |
| Debug AgentQL script                             | [debug_agentql_script](https://github.com/tinyfish-io/fish-tank/tree/main/examples/debug_script)                                                        |
| Run script in headless browser                   | [run_script_in_headless_browser](https://github.com/tinyfish-io/fish-tank/tree/main/examples/run_script_in_headless_browser)                            |
| Run script with an external or existing browser  | [interact_with_an_external_or_existing_browser](https://github.com/tinyfish-io/fish-tank/tree/main/examples/interact_with_external_or_existing_browser) |
| Run script online in Google Colaboratory         | [run_in_google_colab](./examples/run_script_online_in_google_colab)                                                                                     |
| Compare product prices across different websites | [compare_price_across_sites](https://github.com/tinyfish-io/fish-tank/tree/main/examples/compare_product_prices)                                        |
| Save and reuse logged in state                   | [save_and_load_authenticated_session](https://github.com/tinyfish-io/fish-tank/tree/main/examples/save_and_load_authenticated_session)                  |
| Wait for page to load                            | [wait_for_entire_page_load](https://github.com/tinyfish-io/fish-tank/tree/main/examples/wait_for_entire_page_load)                                      |
| Close popup windows (like promotion form)        | [close_popup](https://github.com/tinyfish-io/fish-tank/tree/main/examples/close_popup)                                                                  |
| Close cookie dialog                              | [close_cookie](https://github.com/tinyfish-io/fish-tank/tree/main/examples/close_cookie_dialog)                                                         |
| Leverage List Query                              | [list_query_usage](https://github.com/tinyfish-io/fish-tank/tree/main/examples/list_query_usage)                                                        |
| Leverage get_by_prompt method                    | [get_by_prompt](https://github.com/tinyfish-io/fish-tank/tree/main/examples/get_by_prompt)                                                              |
| Log into Site                                    | [log_into_sites](https://github.com/tinyfish-io/fish-tank/tree/main/examples/log_into_sites)                                                            |

## Application Examples

In this list, you'll find more sophisticated examples that showcase real-world usage scenarios. These examples are designed to illustrate how AgentQL can be applied in more complex and practical situations.

| Topic                                                                 | URL                                                                                                                                      |
| --------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| Getting Xpath of a web element returned by AgentQL                    | [xpath](https://github.com/tinyfish-io/fish-tank/tree/main/application_examples/xpath)                                                   |
| Performing sentiment analysis on YouTube comments gathered by AgentQL | [perform_sentiment_analysis](https://github.com/tinyfish-io/fish-tank/tree/main/application_examples/perform_sentiment_analysis)         |
| Collecting data about products given price range                      | [collect_ecommerce_pricing_data](https://github.com/tinyfish-io/fish-tank/tree/main/application_examples/collect_ecommerce_pricing_data) |
