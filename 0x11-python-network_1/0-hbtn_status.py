#!/usr/bin/python3

if __name__ == "__main__":
    """ HTTP fetch request from a url """
    import urllib.request
 
    url = 'https://alx-intranet.hbtn.io/status'

    # Make the request
    with urllib.request.urlopen(url) as response:
        body = response.read()

    # Response print format
    print("Body response:$")
    print("\t- type:", type(body))
    print("\t- content:", body)
    print("\t- utf8 content:", body.decode('utf-8'))
