#!/usr/bin/python3
"""takes in a 'URL', sends a request to said 'URL',
    and displays the value of the variable 'X-Request-Id',
    found in the header of the response"""
import sys
import requests


if __name__ == "__main__":

    url = sys.argv[1]
    req = requests.get(url)

    print(req.headers.get("X-Request-Id"))
