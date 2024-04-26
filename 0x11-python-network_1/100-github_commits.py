#!/usr/bin/python3
"""
script that takes 2 arguments in order
and prints last 10 commits using githubapi
"""


import sys
import requests

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    headers = {
        "Accept": "application/vnd.github.v3+json"
    }

    # GET request to the GitHub API endpoint
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        commits = response.json()
        for commit in commits[:10]:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
