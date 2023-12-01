#!/usr/bin/python3

# HTTP fetch module
import urllib.request

# URL to fetch data from
url = 'https://alx-intranet.hbtn.io/status'

# Make the request
with urllib.request.urlopen(url) as response:
    body = response.read()

# Response print format
print("Body response:$")
print("\t- type:", type(body))
print("\t- content:", body)
print("\t- utf8 content:", body.decode('utf-8'))
