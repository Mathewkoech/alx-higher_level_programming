#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL and displays the
value of the variable X-Request-Id in the response header
Usage: ./5-hbtn_header.py https://alx-intranet.hbtn.io
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    body_response = response.headers.get('X-Request-Id')
    print(body_response)
