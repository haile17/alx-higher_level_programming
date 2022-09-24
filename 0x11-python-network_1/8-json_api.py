#!/usr/bin/python3
"""
python script that takes in a letter and sends a post request to http://0.0.0.0:5000/search_user using a package requests and sys 
"""

import requests 
import sys 
if __name__ == "__main__":

    me = sys.argv[1] if len(sys.argv) > 1 else ""
    bella = requests.post('http://0.0.0.0:5000/search_user', data={'me': me})
    try:
        haile = bella.json()
        if haile == {}:
            print('No result')
        else:
            print("[{}] {}".format(haile.get('id'), haile.get('name')))
    except ValueError:
        print('Not a valid JSON')
