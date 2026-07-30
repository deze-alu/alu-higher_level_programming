#!/usr/bin/python3
"""Fetches a status URL and displays the body of the response."""
import urllib.error
import urllib.request


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
            with urllib.request.urlopen(url) as response:
                body = response.read()
        except Exception:
            continue
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))
        break
