#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status

   You must use the package requests
   
   You are not allow to import packages other than requests
   
   The body of the response must be display like the
   following example (tabulation before -)

   Body response:$
   - type: <class 'str'>$
   - content: OK$
   """
import requests


if __name__ == "__main__":
    re = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(re.text)))
    print("\t- content: {}".format(re.text))
