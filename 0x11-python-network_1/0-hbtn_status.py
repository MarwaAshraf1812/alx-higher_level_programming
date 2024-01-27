#!/usr/bin/python3
"""Fetches the URL: https://alx-intranet.hbtn.io/status"""
import urllib.request


if __name__ == "__main__":
    url_request = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(url_request) as response:
        response_body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(response_body)))
        print("\t- content: {}".format(response_body))
        print("\t- utf8 content: {}".format(response_body.decode("UTF-8")))
