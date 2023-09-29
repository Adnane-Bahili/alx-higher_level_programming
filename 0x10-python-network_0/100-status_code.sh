#!/bin/bash
# Displays the status code of the response, when sending a 'GET' request to the specified 'URL'
curl -s -o /dev/null -w "%{http_code}" "$1"
