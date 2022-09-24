#!/usr/bin/python3
"""
a python script that takes in a url, sends a request to the URL and displays the 
body of the response(decoded in utf-8 ) that manage urllib.error.HTTPerror
"""

if __name__ == "__main__":
    import urllib.request
    from urllib.error import HTTPError
    import sys

    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print (response.read().decode("utf-8", "replace"))
    except HTTPError as er:
        print ('Error code: {}'.format(er.code))
