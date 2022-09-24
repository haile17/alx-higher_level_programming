#!/usr/bin/python3
"""
python script that takes in a URL and an email address, sends a post request to the passed URL with and email as a parameter, and finally displays the body of the response"""

import sys
import requests
if __name__ == "__main__":
    me = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(me.text)
