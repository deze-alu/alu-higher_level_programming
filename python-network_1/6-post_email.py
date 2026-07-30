#!/usr/bin/python3
"""Sends an email to a URL and displays the body of the response."""
import sys
import requests


if __name__ == "__main__":
    response = requests.post(sys.argv[1], data={"email": sys.argv[2]})
    print(response.text)
