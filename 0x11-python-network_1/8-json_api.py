#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request to
   http://0.0.0.0:5000/search_user with the letter as a parameter.

   The letter must be sent in the variable q

   If no argument is given, set q=""

   If the response body is properly JSON formatted and not empty, display
   the id and name like this: [<id>] <name>

   Otherwise:
   Display Not a valid JSON if the JSON is invalid

   Display No result if the JSON is empty
   """
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) > 1:
        q = argv[1]
    else:
        q = ''

    try:
        url = 'http://0.0.0.0:5000/search_user'
        payload = {'q': q}
        re = requests.post(url, payload).json()

        if {'id', 'name'} <= re.keys():
            print('[{id}] {name}'.format(id=re.get('id'), name=re.get('name')))
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')
