#!/usr/bin/python3
"""takes specific GitHub credentials and uses the GitHub API
    to display an account's id"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":

    cred = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    req = requests.get("https://api.github.com/user", auth=cred)

    print(req.json().get("id"))
