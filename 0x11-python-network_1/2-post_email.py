#!/usr/bin/python3
"""sends a 'POST' request to a given 'URL' with a given email"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":

    url = sys.argv[1]
    val = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(val).encode("utf-8")
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as resp:
        print(resp.read().decode("utf-8"))
