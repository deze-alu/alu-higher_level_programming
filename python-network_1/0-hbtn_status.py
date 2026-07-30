#!/usr/bin/python3
"""Fetches a URL and displays the body of the response."""
import urllib.request


if __name__ == "__main__":
    url = "http://0.0.0.0:5050/status"
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))
