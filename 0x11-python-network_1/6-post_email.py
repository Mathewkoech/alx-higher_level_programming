#!/usr/bin/python3
"""script that takes in a URL and an email, sends a
POST request to the passed URL with
the email as a parameter, and displays the
body of the response (decoded in utf-8)"""


import sys
import requests


if __name__ == "__main__":
    # Extract the URL and email from command-line arguments
    url = sys.argv[1]
    email_address = {"email":sys.argv[2]}
    request = requests.post(url, data=email_address)
    response = request.text
    print(response)
