#!/usr/bin/python3

"""
a python script that takes in a URL and an email,sends a post request to the passes URL with the email as a parameter, and displays the body of the response with a package urllib and sys 
"""

if __name__ == "__main__":
        import sys 
        import urllib.request
        import urllib.parse 

        value = {"email": sys.argv[2]}
        url = sys.argv[1]
        data = urllib.parse.urlencode(value).encode("ascii")

        request = urllib.request.Request(url, data)
        with urllib.request.urlopen(request) as response:
            print(response.read().decode("utf-8"))
