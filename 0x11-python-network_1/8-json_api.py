#!/usr/bin/python3
"""takes in a letter and sends a 'POST' request
    to 'http://0.0.0.0:5000/search_user' with the letter as a parameter"""
import sys
import requests


if __name__ == "__main__":

    lett3r = "" if len(sys.argv) == 1 else sys.argv[1]
    p4ylo4d = {"q": lett3r}
    req = requests.post("http://0.0.0.0:5000/search_user", data=p4ylo4d)

    try:
        resp = req.json()
        if resp == {}:
            print("No result")
        else:
            print("[{}] {}".format(resp.get("id"), resp.get("name")))
    except ValueError:
        print("Not a valid JSON")
