#!/bin/bash
# Sends a GET request to the URL, and displays the body of the response
CUSTOM_H="X-HolbertonSchool-User-Id: 98"
curl -s -H "CUSTOM_H" "${1}"
