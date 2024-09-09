# Stealth mode: Running AgentQL in stealth mode and avoiding bot detection

This example demonstrates how to lower the risk of being detected by a anti-bot system by running AgentQL in stealth mode.

There are several techniques we use in this script to avoid detection:

- randomize various HTTP headers browser sends to the server. This includes `User-Agent`, `Accept-Language`, `Referer`, etc. This helps with consecutive requests looking more like they are coming from different users.
- randomize browser window size. This is important because some websites track the window size and if it's the same for all requests, it's a sign of a bot.
- randomize timezone and geolocation. This is important because some websites track the timezone and geolocation and if it's the same for all requests, it's a sign of a bot.
- (Optional) use a proxy server. You would need to get a Proxy configuration (host, username, password) separately from an external proxy provider (e.g. [NetNut](https://netnut.io), [BrightData](https://brightdata.com/) or similar)

## Run the script

- [Install AgentQL SDK](https://docs.agentql.com/installation/sdk-installation)
  - If you already have SDK installed, make sure to update to the latest version: `pip3 install agentql --upgrade`
- Save this python file locally as **stealth_mode.py**
- Run the following command from the project's folder:

```bash
python3 stealth_mode.py
```
