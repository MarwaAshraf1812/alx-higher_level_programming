#!/bin/bash
#sends a request to that URL, and displays the size of the body of the response
url="$1"
curl -s "$url" | wc -c
