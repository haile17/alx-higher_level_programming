#!/usr/bin/python3
"""
python script that takes in a URL,
sends a request to the URL and displays
value of the variable X-request-id in the
response header using a package requests and sys
"""
import requests
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    url_o = requests.get(url)
    if "X-Request-Id" in url_o.headers:
        print(url_o.headers["X-Request-Id"])
    else:
        print(None)
