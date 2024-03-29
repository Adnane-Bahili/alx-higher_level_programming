#!/usr/bin/python3
"""takes in a 'URL' and sends it a request, displays body of the response"""
import sys
import requests


if __name__ == "__main__":

    url = sys.argv[1]
    req = requests.get(url)

    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)
