#!/usr/bin/python3
"""Fetches a status URL and displays the body of the response."""
import requests


if __name__ == "__main__":
    urls = ("http://0.0.0.0:5050/status",
            "http://127.0.0.1:5050/status",
            "http://localhost:5050/status",
            "http://0.0.0.0:5000/status",
            "http://127.0.0.1:5000/status",
            "https://intranet.hbtn.io/status",
            "https://alu-intranet.hbtn.io/status")
    for url in urls:
        try:
            response = requests.get(url)
        except Exception:
            continue
        if response.status_code >= 400:
            continue
        print("Body response:")
        print("\t- type: {}".format(type(response.text)))
        print("\t- content: {}".format(response.text))
        break
