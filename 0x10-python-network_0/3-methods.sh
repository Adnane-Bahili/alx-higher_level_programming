#!/bin/bash
# Displays the 'HTTP' methods accepted by the server of the provided 'URL'
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
