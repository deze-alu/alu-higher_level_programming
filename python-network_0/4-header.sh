#!/bin/bash
# Sends a GET request with a user id header and displays the body of the response
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1"
