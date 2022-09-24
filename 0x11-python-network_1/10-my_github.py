#!/usr/bin/python3
"""python script that takes a github credential
and uses the github api to display id
using request and sys packages"""
import requests
import sys
from requests.auth import HTTPBasicAuth
if __name__ == "__main__":
    bela = requests.get('https://api.github.com/user',
                        auth=HTTPBasicAuth(sys.argv[1], sys.argv[2]))
    if bela.status_code >= 400:
        print('None')
    else:
        print(bela.json().get('id'))
