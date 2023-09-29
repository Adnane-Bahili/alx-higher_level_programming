#!/bin/bash
# Sends a 'GET' request with a header variable to the specified 'URL'
curl -sH "X-School-User-Id: 98" "$1"
