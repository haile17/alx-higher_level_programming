#!/usr/bin/python3
"""python script that takes 2 arguments in order
to solve repository name
owner name with request and sys packages"""
import requests
import sys
if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
            sys.argv[2], sys.argv[1])
    r = requests.get(url)
    commit = r.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commit[i].get("sha"),
                commit[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
