#!/usr/bin/python3
"""lists the 10 most recent commits of a github repository"""
import sys
import requests


if __name__ == "__main__":

    url = "https://api.github.com/repos/{}/{}/commits".\
            format(sys.argv[2], sys.argv[1])
    req = requests.get(url)
    comms = req.json()

    try:
        for r in range(10):
            print("{}: {}".format(
                comms[r].get("sha"),
                comms[r].get("commit").get("author").get("name")))
    except IndexError:
        pass
