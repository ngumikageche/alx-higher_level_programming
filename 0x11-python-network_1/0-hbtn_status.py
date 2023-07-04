#!/usr/bin/python3
"""a script that fetches """
import urllib.request


if __name__ == "__main__":
    request_url = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(request_url) as response:
        body = response.read()
        print("Body respose:")
        print("\t-  type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))
        
