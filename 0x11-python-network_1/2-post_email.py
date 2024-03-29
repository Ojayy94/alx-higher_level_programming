#!/usr/bin/python3
"""Python script that takes in a URL and an email, sends a POST request to the
   passed URL with the email as a parameter, and displays
   the body of the response (decoded in utf-8)
   """
from urllib.request import urlopen, Request
from urllib.parse import urlencode
import sys


if __name__ == "__main__":
    data = urlencode({
                        "email": sys.argv[2]
                    }).encode("ascii")
    req = Request(sys.argv[1], data)

    with urlopen(req) as res:
        print(res.read().decode("utf-8"))
