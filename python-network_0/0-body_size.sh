#!/bin/bash
# Sends a request to the URL passed as argument and displays the body size in bytes
curl -s "$1" | wc -c
