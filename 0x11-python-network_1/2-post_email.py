#!/usr/bin/python3
"""script takes in URL and email and sends
a post request using urllib and sys package
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
