# Yesterweb Webring Checker

I built this tool to periodically monitor the HTTP status of websites belonging to the [webring](https://yesterweb.org/webring/members.html).

It currently lives [here](https://ring-status.yesterweb.org/).

## What it Does
This parses a JSON file, grabs the values named "url", and then publishes the values to an HTML file.

## How to Use
1. Clone the directory locally
2. Install Python 3 and Pip
3. Run `python3 main.py` on Ubuntu or `py main.py` on Windows

It will generate an HTML file and a log file in the directory that you run it from. 