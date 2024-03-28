#!/bin/bash
# Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
# YDisplay only body of a 200 status code response
# You have to use curl

curl -sL "$1" -X GET -D ./header -o ./output; if grep -q "200 OK" ./header; then cat ./output; fi
