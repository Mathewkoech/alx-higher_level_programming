#!/usr/bin/python3
"""
script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 2:
        letter = sys.argv[1]
    else:
        letter = ""
    url = "http://0.0.0.0:5000/search_user"

    response = requests.post(url, data={"q": letter})
    try:
        json_data = response.json()
        if json_data:
            print("{[]} {}".format(json_data['id']. json_data['name']))
        else:
            print("Not a valid JSON")
    except ValueError:
        print("No result")
