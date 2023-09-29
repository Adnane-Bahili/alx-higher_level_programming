#!/usr/bin/python3
"""takes in a 'URL', sends a request to the 'URL',
    displays the body of the response"""
import sys
import urllib.error
import urllib.request


if __name__ == "__main__":

    url = sys.argv[1]
    req = urllib.request.Request(url)

    try:
        with urllib.request.urlopen(req) as resp:
            print(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as err:
        print("Error code: {}".format(err.code))
