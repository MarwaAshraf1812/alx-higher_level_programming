#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status"""
import requests


if __name__ == "__main__":
    url = requests.get("https://alx-intranet.hbtn.io/status")
    t = url.text
    print("Body response:")
    print("\t- type: {}\n\t- content: {}".format(type(t), t))
