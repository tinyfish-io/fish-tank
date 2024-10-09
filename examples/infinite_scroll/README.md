# Example script: load additional content on page by scrolling

This example demonstrates how to load additional content on pages that load content based on scroll position

## Run the script

- [Install AgentQL SDK](https://docs.agentql.com/installation/sdk-installation)
- Save this python file locally as **infinite_scroll.py**
- Run the following command from the project's folder:

```bash
python3 infinite_scroll.py
```

## Adjust the scrolling method

Dynamically loading content can be tricky to get right, as websites have a lot of ways to customize how this interaction looks on their sites.

Scrolling to the end of a page by pressing the `End` key is not always a reliable mechanism, since pages could either have multiple scrollable areas, or have the `End` key mapped to a different function, such as for video playback. Try replacing `key_press_end_scroll(page)` in the example with `mouse_wheel_scroll(page)` and observe how the browser behaves differently, or try navigating to your own site to test in `page.goto`!
