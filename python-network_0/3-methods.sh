#!/bin/bash
# Displays all the HTTP methods the server of the URL passed as argument accepts
curl -sI -X OPTIONS "$1" | grep -i '^allow:' | cut -d' ' -f2- | tr -d '\r'
