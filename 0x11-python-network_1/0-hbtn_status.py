#!/usr/bin/python3
"""fetches given URL"""
import urllib.request


if __name__ == "__main__":

    req = urllib.request.Request("https://alx-intranet.hbtn.io/status")

    with urllib.request.urlopen(req) as resp:
        bd = resp.read()
        print("Body response:")
        print("\t- type: {}".format(type(bd)))
        print("\t- content: {}".format(bd))
        print("\t- utf8 content: {}".format(bd.decode("utf-8")))
