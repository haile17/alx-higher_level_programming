#!/usr/bin/python3
"""
python script that takes in a URL,
sends a request to the URL and displays
the body of the response with a package requests and sys"""

import requests
import sys
from sys import argv
if __name__ == "__main__":
    me = requests.get(argv[1])
    if me.status_code >= 400:
        print("Error code: {}".format(me.status_code))
    else:
        print(me.text)
