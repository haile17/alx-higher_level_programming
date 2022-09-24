#!/usr/bin/python3
"""
write a python script that takes in a URL, sends a request to the url and displays the value of the x-request-Id variable found in the header of the response and uses the package urllib and sys 
"""
 
if __name__ == "__main__":
    import urllib.request
    import sys

    with urllib.request.urlopen(sys.argv[1]) as response:
        head = response.headers.get('X-request-Id')
        print(head)
