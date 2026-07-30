#!/usr/bin/python3
"""Fetches a URL and displays the body of the response."""
import requests


if __name__ == "__main__":
    response = requests.get("http://0.0.0.0:5050/status")
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
