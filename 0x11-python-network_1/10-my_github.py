#!/usr/bin/python3
"""
Python script that takes GitHub credentials
and uses the GitHub API to display the user id
"""
from requests import get, auth
import sys


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    user_name = sys.argv[1]
    user_password = sys.argv[2]
    res = get(url, auth=auth.HTTPBasicAuth(user_name, user_password))
    print(res.json().get('id'))
