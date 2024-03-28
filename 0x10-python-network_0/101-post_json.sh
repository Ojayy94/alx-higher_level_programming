#!/bin/bash
# This program sends a request to a URL passed as an argument, and displays only the status code of the response.
curl -s "$1" -X POST -H "Content-Type: application/json" -d "$(cat "$2")"
