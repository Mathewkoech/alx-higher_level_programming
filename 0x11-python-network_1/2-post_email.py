#!/usr/bin/python3
"""script that takes in a URL and an email, sends a POST request to the passed URL with 
the email as a parameter, and displays the body of the response (decoded in utf-8)"""


import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    # Extract the URL and email from command-line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Encode the email data
    data = urllib.parse.urlencode({'email': email})
    data = data.encode('utf-8')

    # Create a POST request
    req = urllib.request.Request(url, data=data, method='POST')
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
