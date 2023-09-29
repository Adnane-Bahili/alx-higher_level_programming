#!/bin/bash
# Sends a 'JSON' 'POST' request to the specifed 'URL' with a given JSON file
# Displays the body of the response
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
