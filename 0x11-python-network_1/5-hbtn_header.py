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
    r = requests.Request(sys.argv[1])
    print(r.headers.get("X-requests-Id"))
