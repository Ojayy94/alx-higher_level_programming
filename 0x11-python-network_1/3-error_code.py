#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL
   and displays the body of the response (decoded in utf-8).

   You have to manage urllib.error.HTTPError exceptions and
   print: Error code: followed by the HTTP status code

   You must use the packages urllib and sys

   You are not allowed to import other packages than urllib and sys

    You don’t need to check arguments passed to the script (number or type)

    You must use the with statement
    """
import sys
from urllib.request import urlopen, Request
from urllib.error import HTTPError
from urllib.parse import urlencode


if __name__ == "__main__":
    req = Request(sys.argv[1])

    try:
        with urlopen(req) as res:
            print(res.read().decode("utf-8"))
    except HTTPError as err:
        print("Error code: {}".format(err.code))
